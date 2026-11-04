
import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("RUST VISION")
root.geometry("500x430")
root.configure(bg="#10131b")
root.resizable(False, False)

menu_open = True
glow_enabled = True
boxes_enabled = True
glow_color = "#a855f7"

def toggle_glow():
    global glow_enabled
    glow_enabled = not glow_enabled
    glow_button.config(
        text=f"Glow: {'ON' if glow_enabled else 'OFF'}"
    )

def toggle_boxes():
    global boxes_enabled
    boxes_enabled = not boxes_enabled
    boxes_button.config(
        text=f"Boxes: {'ON' if boxes_enabled else 'OFF'}"
    )

def change_color():
    global glow_color
    selected = colorchooser.askcolor()[1]
    if selected:
        glow_color = selected
        color_button.config(bg=selected)

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
    font=("Arial", 25, "bold"),
    fg="#b875ff",
    bg="#10131b"
)
title.pack(pady=20)

tk.Label(
    root,
    text="VISUAL OVERLAY SETTINGS",
    fg="#858da5",
    bg="#10131b"
).pack(pady=5)

glow_button = tk.Button(
    root, text="Glow: ON",
    command=toggle_glow,
    width=25
)
glow_button.pack(pady=12)

boxes_button = tk.Button(
    root, text="Boxes: ON",
    command=toggle_boxes,
    width=25
)
boxes_button.pack(pady=12)

color_button = tk.Button(
    root, text="Choose color",
    command=change_color,
    bg=glow_color,
    width=25
)
color_button.pack(pady=12)

tk.Label(
    root,
    text="INSERT - OPEN / CLOSE MENU",
    fg="#b875ff",
    bg="#10131b"
).pack(pady=25)

tk.Label(
    root,
    text="Standalone UI prototype",
    fg="#666b7c",
    bg="#10131b"
).pack()

root.mainloop()
