"""
View file
"""

from tkinter import Tk, Frame
from abc import abstractmethod


class View(Frame):
    """
    Parent View class
    Applies template to all children
    Requires render method in children
    """
    def __init__(self, root: Tk, data: dict = None, **kw):
        super().__init__(**kw)
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
