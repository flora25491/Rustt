
import tkinter as tk
from menu import VisionMenu
from settings import load_settings, save_settings

settings = load_settings()

root = tk.Tk()
root.title("RUST VISION")
root.geometry("750x500")
root.configure(bg="#101019")
root.resizable(False, False)

VisionMenu(root)

def toggle_menu(event=None):
    if root.state() == "withdrawn":
        root.deiconify()
    else:
        root.withdraw()

root.bind("<Insert>", toggle_menu)

def close_app():
    save_settings(settings)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()
