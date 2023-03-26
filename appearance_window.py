import json
from tkinter import *
from tkinter import ttk
import os


class Appearance(Toplevel):
    def __init__(self, theme):
        super().__init__()
        self.theme = theme

        self.icon = PhotoImage(file="images/apear.png")
        self.iconphoto(False, self.icon)
        self.geometry("300x200")
        self.minsize(350, 200)
        self.maxsize(350, 200)
        self.title("Appearance")
        self.config(bg=theme["bg"])

        # menu frame

        self.menu_prev = Frame(self, bg=theme["menu"])
        self.menu_prev.pack(side=LEFT, fill=BOTH)

        self.theme_hint = Label(self.menu_prev, text="Select theme", font=("Arial", 15, "bold"), bg=theme["menu"],
                                fg=theme["text-menu"])
        self.theme_hint.pack(pady=5)

        self.combox = ttk.Combobox(self.menu_prev, state="readonly",
                                   values=list(map(lambda x: x[:-5], os.listdir("themes"))))
        self.combox.pack(pady=5, padx=5)
        self.combox.bind("<<ComboboxSelected>>", self.select_theme)

        self.needs_res = Label(self.menu_prev, text="App restart required", font=("Arial", 10, "bold"),
                               bg=theme["menu"], fg=theme["text-menu"])
        self.needs_res.pack()

        self.prev_seg = Frame(self.menu_prev, bg=theme["segment"])
        self.prev_seg.pack(fill=X, padx=5, pady=5)

        self.prev_hint = Label(self.prev_seg, bg=theme["segment"], fg=theme["text-menu"], font=("Arial", 10, "bold"),
                               text="Preview entry")
        self.prev_hint.pack()

        self.prev_entry = Entry(self.prev_seg, bg=theme["entry-menu"], fg=theme["entry-menu-text"], border=FALSE)
        self.prev_entry.pack(pady=5)

        self.prev_btn = Button(self.menu_prev, text="Preview button", bg=theme["button-bg"], fg=theme["button-text"],
                               border=FALSE, highlightthickness=0, cursor="hand2")
        self.prev_btn.pack(fill=X, pady=5, padx=5)

        # description frame

        self.prev_desc = Frame(self, bg=theme["bg"])
        self.prev_desc.pack(side=RIGHT, fill=BOTH, expand=TRUE)

        self.prev_desc_lbl = Label(self.prev_desc, text="Preview text", bg=theme["bg"], fg=theme["text-desc"],
                                   font=("Arial", 20, "bold"))
        self.prev_desc_lbl.pack()

        self.prev_entry_desc = Entry(self.prev_desc, bg=theme["entry-desc"], fg=theme["entry-desc-text"], border=FALSE)
        self.prev_entry_desc.pack(fill=X, padx=5)

        self.prev_step_frame = Frame(self.prev_desc, bg=theme["bg"])
        self.prev_step_frame.pack(fill=X)

        self.prev_step = Label(self.prev_step_frame, text="1. Preview checkbutton", bg=theme["bg"],
                               fg=theme["text-desc"], font=("Arial", 10, "bold"))
        self.prev_step.pack(side=LEFT)

        self.prev_check = Checkbutton(self.prev_step_frame, bg=theme["bg"], activebackground=theme["bg"],
                                      fg=theme["check-colour"], cursor="hand2")
        self.prev_check.pack(side=RIGHT)

    def select_theme(self, event) -> None:
        with open("config.json") as config_file:
            config = json.load(config_file)

        config["theme"] = self.combox.get()

        with open("config.json", "w") as config_file:
            json.dump(config, config_file, ensure_ascii=False, indent=2)
