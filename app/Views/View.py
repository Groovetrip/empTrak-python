"""
View file
"""

from typing import Callable
from tkinter import Tk
from abc import abstractmethod


class View:
    """
    Parent View class
    Applies template to all children
    Requires render method in children
    """
    def __init__(self, emit_callback: Callable, root: Tk, data: dict = None):
        self.emit_callback = emit_callback
        self.root = root
        self.data = data
        self.apply_template()

    def emit(self, key: str):
        """
        Emit key to Controller callback
        """
        self.emit_callback(key)
        return

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
