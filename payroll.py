"""
EmpTrak
Group 2
CS-2450-601
Professor Sharp
"""

from abc import ABC, abstractmethod

PAY_LOG_FILE = 'paylog.txt'
EMPLOYEES = []

class Employee:
    """
    Employee model
    Instances represent one employee entry in storage
    """

    # Disable instance attributes warning: All instance attributes are required.
    # pylint: disable=too-many-instance-attributes

    def __init__(self, emp_id, name, address, city, state, zipcode):
        self.id_ = emp_id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = None
        self.paymethod = None

    def make_hourly(self, rate):
        """
        Assigns the Hourly payment classification to employee
        :param float rate: Hourly pay
        :rtype: None
        """
        self.classification = Hourly(rate)

    def make_salaried(self, salary):
        """
        Assigns the Salaried payment classification to employee
        :param float salary: Annual pay
        :rtype: None
        """
        self.classification = Salaried(salary)

    def make_commissioned(self, salary, rate):
        """
        Assigns the Commissioned payment classification to employee
        :param float salary: Annual pay
        :param float rate: Commission rate
        :rtype: None
        """
        self.classification = Commissioned(salary, rate)

    def mail_method(self):
        """
        Assigns the MailMethod payment method to employee
        :rtype: None
        """
        self.paymethod = MailMethod(self)

    def direct_method(self, routing_number, account_number):
        """
        Assigns the DirectMethod payment method to employee
        :param float routing_number: The employee's bank routing number
        :param float account_number: The employee's bank account number
        :rtype: None
        """
        self.paymethod = DirectMethod(self, routing_number, account_number)

    def issue_payment(self, file_name):
        """
        Calculates payment and issues it to employee using their payment method
        :rtype: None
        :raises: TypeError
        """
        if self.classification is None:
            raise TypeError('Cannot issue payment: Employee has no classification.')
        if self.paymethod is None:
            raise TypeError('Cannot issue payment: Employee has no pay method.')
        pay_amount = self.classification.compute_pay()
        return self.paymethod.issue(pay_amount, file_name)


class PaymentMethod(ABC):
    """
    Pay method parent class
    Children must define an issue() method for issuing employee payments
    """

    # Disable too few public methods warning: Only one public method is required
    # pylint: disable=too-few-public-methods

    def __init__(self, employee):
        self.employee = employee

    @abstractmethod
    def issue(self, pay_amount, file_name):
        """
        Issues payment to employee
        :param str file_name: Pay log file name
        :param float pay_amount: Amount to pay employee
        :rtype: None
        """


class DirectMethod(PaymentMethod):
    """
    Direct payment method class
    Inherits PaymentMethod
    Issues payments directly to employee bank account
    """

    # Disable too few public methods warning: Only one public method is required
    # pylint: disable=too-few-public-methods

    def __init__(self, employee, routing_number, account_number):
        self.routing_number = routing_number.strip()
        self.account_number = account_number.strip()
        super().__init__(employee)

    def issue(self, pay_amount, file_name):
        """
        Issues payment to employee, appends transaction to payment log
        :param str file_name: Payment log file name
        :param float pay_amount: Amount to pay employee
        :rtype: None
        """
        with open(file_name, 'a') as file:
            file.write(f'Transferred {pay_amount:.2f} for {self.employee.name} to'
                       f' {self.account_number} at {self.routing_number}\n')


class MailMethod(PaymentMethod):
    """
    Mail payment method class
    Inherits PaymentMethod
    Issues payment to employee address via mail
    """

    # Disable too few public methods warning: Only one public method is required
    # pylint: disable=too-few-public-methods

    def issue(self, pay_amount, file_name):
        """
        Issues payment to employee, appends transaction to payment log
        :param str file_name: Payment log file name
        :param float pay_amount: Amount to pay employee
        :rtype: None
        """
        with open(file_name, 'a') as file:
            file.write(f'Mailing {pay_amount:.2f} to {self.employee.name} at'
                       f' {self.employee.address} {self.employee.city} {self.employee.state}'
                       f' {self.employee.zipcode}\n')


class Classification(ABC):
    """
    Pay classification parent class
    Children must define a compute_pay() method for calculating employee pay
    """

    # Disable too few public methods warning: Only one public method is required
    # pylint: disable=too-few-public-methods

    @abstractmethod
    def compute_pay(self):
        """
        Calculates and returns employee pay
        :rtype: float
        """


class Hourly(Classification):
    """
    Hourly pay classification class
    Inherits Classification
    Used to assign hourly pay rate to employee
    """
    def __init__(self, rate):
        self.rate = float(rate)
        self.timecards = []
        super().__init__()

    def add_timecard(self, timecard_hours):
        """
        Adds recorded timeclock hours between punch in and punch out
        :param float timecard_hours: Hours worked
        :rtype: None
        """
        self.timecards.append(float(timecard_hours))

    def compute_pay(self):
        """
        Calculates and returns employee pay
        :rtype: float
        """
        pay_amount = 0
        for i in self.timecards:
            pay_amount = i*self.rate
        self.timecards = []
        return pay_amount


class Salaried(Classification):
    """
    Salaried pay classification class
    Inherits Classification
    Used to assign salaried pay rate to employee
    """

    # Disable too few public methods warning: Only one public method is required
    # pylint: disable=too-few-public-methods

    def __init__(self, salary):
        self.salary = float(salary)
        super().__init__()

    def compute_pay(self):
        """
        Calculates and returns employee pay
        :rtype: float
        """
        return self.salary/24


class Commissioned(Salaried):
    """
    Commissioned pay classification class
    Inherits Salaried
    Used to assign commissioned pay rate to employee
    """
    def __init__(self, salary, commission_rate):
        self.commission_rate = float(commission_rate)
        self.receipts = []
        super().__init__(salary)

    def add_receipt(self, receipt_amount):
        """
        Records sale amount for commission calculation
        :param float receipt_amount: Sale total on receipt
        :rtype: None
        """
        self.receipts.append(float(receipt_amount))

    def compute_pay(self):
        """
        Calculates and returns employee pay
        :rtype: float
        """
        pay_amount = self.salary/24
        for i in self.receipts:
            pay_amount += i*(self.commission_rate/100)
        self.receipts = []
        return pay_amount


def load_employees():
    """
    Instantiate Employee objects from employee data
    Assign employees payment methods and payment classifications
    Append employees to EMPLOYEES array
    :rtype: None
    """
    with open('employees.csv') as file:
        lines = file.readlines()
        for i in range(1, len(lines)):
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
    """
    Reads and stores employee timeclock hours
    Employees must exist and have the Hourly payment classification
    :rtype: None
    :raises: TypeError|Exception
    """
    with open('timecards.txt', 'r') as file:
        timecards = file.readlines()
        for timecard in timecards:
            data = timecard.split(',')
            employee = find_employee_by_id(data[0])
            if employee is None:
                raise Exception('Employee not found')
            if not isinstance(employee.classification, Hourly):
                raise TypeError('Employee classification is not Hourly')
            for i in range(1, len(data)):
                employee.classification.add_timecard(float(data[i].strip()))


def process_receipts():
    """
    Reads and stores employee receipt amounts
    Employees must exist and have the Commissioned payment classification
    :rtype: None
    :raises: TypeError|Exception
    """
    with open('receipts.txt', 'r') as file:
        receipts = file.readlines()
        for receipt in receipts:
            data = receipt.split(',')
            employee = find_employee_by_id(data[0])
            if employee is None:
                raise Exception('Employee not found')
            if not isinstance(employee.classification, Commissioned):
                raise TypeError('Employee classification is not Commissioned')
            for i in range(1, len(data)):
                employee.classification.add_receipt(float(data[i].strip()))


def run_payroll():
    """
    Removes existing payroll files and generates and issues employee payments
    :rtype: None
    """
    # if os.path.exists('paylog.txt'):
    #     os.remove('paylog.txt')
    # if os.path.exists('paylog_old.txt'):
    #     os.remove('paylog_old.txt')
    for emp in EMPLOYEES:
        emp.issue_payment(PAY_LOG_FILE)


def find_employee_by_id(emp_id):
    """
    Searches EMPLOYEES array for employee with matching id
    :param str emp_id: Employee id to search by
    :rtype: Employee|None
    """
    employees = [emp for emp in EMPLOYEES if emp.id_ == emp_id]
    if len(employees) > 0:
        return employees[0]
    return None
