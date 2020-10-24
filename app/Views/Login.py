"""
Login View file
"""

from .View import View
import tkinter


class Login(View):
    """
    Login View class
    Renders app's login page
    """
    def __init__(self, *args):
        super().__init__(*args)

    def render(self):
        """
        Render components for login view
        """
        print('Login.render()')
        button = tkinter.Button(self.root, text='Login')
        button.config(command=lambda: self.emit('login'))
        button.pack()
        return
