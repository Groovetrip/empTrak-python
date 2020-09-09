# Alex Adams
# CS-1410-003
# Professor Allison
# 10-31-19

import os
import shutil
from abc import ABC, abstractmethod

PAY_LOGFILE = 'paylog.txt'
EMPLOYEES = []

class Employee():
    def __init__(self, emp_id, name, address, city, state, zipcode):
        self.id = emp_id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def make_hourly(self, rate):
        self.classification = Hourly(rate)

    def make_salaried(self, salary):
        self.classification = Salaried(salary)

    def make_commissioned(self, salary, rate):
        self.classification = Commissioned(salary, rate)

    def mail_method(self):
        self.paymethod = MailMethod(self)

    def direct_method(self, routing_number, account_number):
        self.paymethod = DirectMethod(self, routing_number, account_number)

    def issue_payment(self):
        pay_amount = self.classification.compute_pay()
        return self.paymethod.issue(pay_amount)


class PaymentMethod(ABC):
    def __init__(self, employee):
        self.employee = employee

    @abstractmethod
    def issue(self, pay_amount):
        pass


class DirectMethod(PaymentMethod):
    def __init__(self, employee, routing_number, account_number):
        self.routing_number = routing_number.strip()
        self.account_number = account_number.strip()
        super().__init__(employee)

    def issue(self, pay_amount):
        with open('paylog.txt', 'a') as f:
            f.write(f'Transferred {pay_amount:.2f} for {self.employee.name} to {self.account_number} at {self.routing_number}\n')


class MailMethod(PaymentMethod):
    def __init__(self, employee):
        super().__init__(employee)

    def issue(self, pay_amount):
        with open('paylog.txt', 'a') as f:
            f.write(f'Mailing {pay_amount:.2f} to {self.employee.name} at {self.employee.address} {self.employee.city} {self.employee.state} {self.employee.zipcode}\n')


class Classification(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def compute_pay(self):
        pass


class Hourly(Classification):
    def __init__(self, rate):
        self.rate = float(rate)
        self.timecards = []
        super().__init__()

    def add_timecard(self, timecard_hours):
        self.timecards.append(float(timecard_hours))

    def compute_pay(self):
        pay_amount = 0
        for i in self.timecards:
            pay_amount = i*self.rate
        self.timecards = []
        return pay_amount


class Salaried(Classification):
    def __init__(self, salary):
        self.salary = float(salary)
        super().__init__()

    def compute_pay(self):
        return self.salary/24


class Commissioned(Salaried):
    def __init__(self, salary, commission_rate):
        self.commission_rate = float(commission_rate)
        self.receipts = []
        super().__init__(salary)

    def add_receipt(self, receipt_amount):
        self.receipts.append(float(receipt_amount))

    def compute_pay(self):
        pay_amount = self.salary/24
        for i in self.receipts:
            pay_amount += i*(self.commission_rate/100)
        self.receipts = []
        return pay_amount


def load_employees():
    with open('employees.csv') as f:
        lines = f.readlines()
        for i in range(1,len(lines)):
            row = lines[i].split(',')
            emp = Employee(row[0], row[1], row[2], row[3], row[4], row[5])
            if row[6] == '1':
                emp.make_hourly(row[9])
            elif row[6] == '2':
                emp.make_salaried(row[8])
            elif row[6] == '3':
                emp.make_commissioned(row[8], row[10])
            if row[7] == '1':
                emp.direct_method(row[11], row[12])
            elif row[7] == '2':
                emp.mail_method()
            EMPLOYEES.append(emp)


def process_timecards():
    with open('timecards.txt', 'r') as f:
        timecards = f.readlines()
        for timecard in timecards:
            data = timecard.split(',')
            emp_class = find_employee_by_id(data[0]).classification
            for i in range(1,len(data)):
                emp_class.add_timecard(float(data[i].strip()))


def process_receipts():
    with open('receipts.txt', 'r') as f:
        receipts = f.readlines()
        for receipt in receipts:
            data = receipt.split(',')
            emp_class = find_employee_by_id(data[0]).classification
            for i in range(1,len(data)):
                emp_class.add_receipt(float(data[i].strip()))


def run_payroll():
    # if os.path.exists('paylog.txt'):
    #     os.remove('paylog.txt')
    # if os.path.exists('paylog_old.txt'):
    #     os.remove('paylog_old.txt')
    for emp in EMPLOYEES:
        emp.issue_payment()


def find_employee_by_id(emp_id):
    return [emp for emp in EMPLOYEES if emp.id == emp_id][0]
