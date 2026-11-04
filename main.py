
import tkinter as tk
from tkinter import colorchooser
from settings import load_settings, save_settings

settings = load_settings()

root = tk.Tk()
root.title("RUST VISION")
root.geometry("520x460")
root.configure(bg="#10131b")
root.resizable(False, False)

menu_open = True

def update_settings():
    save_settings(settings)

def toggle_glow():
    settings["glow"] = not settings["glow"]
    glow_button.config(
        text=f"GLOW: {'ON' if settings['glow'] else 'OFF'}"
    )
    update_settings()

def toggle_boxes():
    settings["boxes"] = not settings["boxes"]
    boxes_button.config(
        text=f"BOXES: {'ON' if settings['boxes'] else 'OFF'}"
    )
    update_settings()

def change_color():
    selected = colorchooser.askcolor(
        color=settings["color"]
    )[1]

    if selected:
        settings["color"] = selected
        title.config(fg=selected)
        color_button.config(bg=selected)
        update_settings()

def toggle_menu(event=None):
    global menu_open
    menu_open = not menu_open

    if menu_open:
        root.deiconify()
    else:
        root.withdraw()

root.bind("<Insert>", toggle_menu)

title = tk.Label(
    root,
    text="RUST VISION",
    font=("Arial", 27, "bold"),
    fg=settings["color"],
    bg="#10131b"
)
title.pack(pady=30)

tk.Label(
    root,
    text="VISUAL OVERLAY",
    font=("Arial", 10),
    fg="#858da5",
    bg="#10131b"
).pack()

glow_button = tk.Button(
    root,
    text=f"GLOW: {'ON' if settings['glow'] else 'OFF'}",
    command=toggle_glow,
    width=28
)
glow_button.pack(pady=15)

boxes_button = tk.Button(
    root,
    text=f"BOXES: {'ON' if settings['boxes'] else 'OFF'}",
    command=toggle_boxes,
    width=28
)
boxes_button.pack(pady=10)

color_button = tk.Button(
    root,
    text="CHANGE COLOR",
    command=change_color,
    bg=settings["color"],
    width=28
)
color_button.pack(pady=15)

tk.Label(
    root,
    text="INSERT - OPEN / CLOSE MENU",
    fg=settings["color"],
    bg="#10131b"
).pack(pady=30)

root.mainloop()
