"""
The main executable file
Compile distributions from this file
"""

# import sqlite3
from os import path
import tkinter as tk
from app.Controller import Controller


DB_NAME = 'empTrak'


def main():
    """
    Turn on the lights.
    Initialize Controller and Root, then begin loop
    """
    global DB_NAME

    root = tk.Tk()

    # TODO: Set tkinter window dimensions, title, etc.

    app = Controller(root)
    app.withdraw()
    app.mainloop()

    if path.exists(f'./database/{DB_NAME}.db'):
        setup(app)
    else:
        app.show_login()


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
