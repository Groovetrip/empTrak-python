"""
Controller class file
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

    def mainloop(self):
        """
        Call mainloop on root
        """
        self.root.mainloop()

    def view(self, view_class: Type[View], data: dict = None):
        """
        Apply view to root
        :param View view_class:
        :param dict|None data:
        """

        if data is None:
            data = {}

        if self.user is None:
            view_class = Login

        emit_callback = self.handle_emit

        # TODO: Clear current root GUI

        view = view_class(self.handle_emit, self.root, data)
        view.render()
        return

    def handle_emit(self, key: str, data: dict = None):
        """

        """
        if key == 'show_dashboard':
            self.show_dashboard()

        if key == 'list_employees':
            self.list_employees()

        if key == 'login':
            self.login(data)

        return

    def login(self, data: dict):
        """
        Validate login using data credentials
        :param dict data:
        """
        return

    def show_setup(self):
        """
        Display first-time setup view
        """
        # self.view(Setup)
        return

    def show_login(self):
        """
        Display login view
        """
        self.view(Login)
        return

    def show_dashboard(self):
        """
        Display dashboard view
        """
        # self.view(Dashboard)
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

    def list_employees(self):
        """
        Display employees index view
        """
        employees = Employee.all()
        self.view(ListEmployees, {
            'employees': employees
        })
        return
