# main.py - Entry point

import tkinter as tk
from gui import CubeGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = CubeGUI(root)
    root.mainloop()
