"""
The main executable
Compile distributions from this file
"""

import tkinter as tk
from .app.Controller import Controller


def main():
    """
    Turn on the lights.
    Initialize Controller and Root, then begin loop
    """
    root = tk.Tk()
    root.withdraw()
    app = Controller(root)
    app.show_login()
    root.mainloop()


if __name__ == '__main__':
    main()
