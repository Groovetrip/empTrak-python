"""

"""

from tkinter import Tk
from abc import abstractmethod
from ..Controller import Controller


class View:
    """
    Parent View class
    Requires
    """
    def __init__(self, controller: Controller, root: Tk, data: dict = None):
        if data is None:
            data = {}
        self.controller = controller
        self.root = root
        self.data = data
        self.apply_template()

    def apply_template(self):
        """
        Render standard view layout
        Navbar, background, etc.
        """
        pass

    @abstractmethod
    def render(self):
        """
        Render tkinter components
        """
        pass
