
import tkinter as tk

BG = "#101019"
PANEL = "#191927"
PURPLE = "#a855f7"
TEXT = "#eeeeff"

class VisionMenu:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg=BG)

        self.sidebar = tk.Frame(root, bg=PANEL, width=140)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar,
            text="RUST\nVISION",
            font=("Arial", 18, "bold"),
            fg=PURPLE,
            bg=PANEL
        ).pack(pady=30)

        self.content = tk.Frame(root, bg=BG)
        self.content.pack(
            side="right",
            expand=True,
            fill="both"
        )

        for name in ["HOME", "VISUALS", "SETTINGS", "ABOUT"]:
            tk.Button(
                self.sidebar,
                text=name,
                command=lambda n=name: self.show_page(n),
                bg=PANEL,
                fg=TEXT,
                activebackground=PURPLE,
                activeforeground="white",
                relief="flat",
                width=16,
                pady=12
            ).pack(pady=5)

        self.show_page("HOME")

    def show_page(self, name):
        for widget in self.content.winfo_children():
            widget.destroy()

        tk.Label(
            self.content,
            text=name,
            font=("Arial", 24, "bold"),
            fg=PURPLE,
            bg=BG
        ).pack(anchor="w", padx=30, pady=30)

        descriptions = {
            "HOME": "Welcome to RUST VISION",
            "VISUALS": "Visual interface settings",
            "SETTINGS": "Application preferences",
            "ABOUT": "RUST VISION - Version 1.0"
        }

        tk.Label(
            self.content,
            text=descriptions[name],
            fg=TEXT,
            bg=BG,
            font=("Arial", 12)
        ).pack(anchor="w", padx=30)
