"""
The main executable file
Compile distributions from this file
"""

# import sqlite3
from os import path
import tkinter
from app.Controller import Controller


DB_NAME = 'empTrak'


def main():
    """
    Turn on the lights.
    Initialize Controller and Root, then begin loop
    """
    global DB_NAME

    root = tkinter.Tk()

    # TODO: Set tkinter window dimensions, title, etc.

    app = Controller(root)
    app.mainloop()


def setup(app: Controller):
    """
    Perform first-time setup
    Create database
    :param Controller app:
    """
    app.show_setup()
    # Set up DB
    return


if __name__ == '__main__':
    main()
