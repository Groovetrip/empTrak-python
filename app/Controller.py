"""

"""

from typing import Type
from tkinter import Tk
from .Models.Employee import Employee
from .Views.View import View
from .Views.Login import Login
from .Views.ShowEmployee import ShowEmployee
from .Views.ListEmployees import ListEmployees


class Controller:
    """
    The Controller class

    Handles routing in our application, and organizes
    data between our model and view classes.
    """
    def __init__(self, root: Tk):
        self.user = None
        self.root = root
        self.show_login()

    def view(self, view_class: Type[View], data: dict = None):
        """
        Apply view to root
        :param View view_class:
        :param dict|None data:
        """

        # TODO: Clear current root GUI

        if self.user is None:
            view = Login(self, self.root)
        else:
            view = view_class(self, self.root, data)

        view.render()
        return

    def login(self, data: dict):
        """
        Validate login using data credentials
        :param dict data:
        """
        return

    def show_login(self):
        """
        Display login view
        """
        self.view(Login)
        return

    def show_employee(self, emp_id: int):
        """
        Display employee details view
        :param int emp_id:
        """
        employee = Employee.find(emp_id)
        self.view(ShowEmployee, {
            'employee': employee
        })
        return

    def index_employees(self):
        """
        Display employees index view
        """
        employees = Employee.all()
        self.view(ListEmployees, {
            'employees': employees
        })
        return
