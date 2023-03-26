from tkinter import *
import appearance_window as apr_w
import theme_reader
import os

themes = theme_reader.get_themes()
theme = themes[theme_reader.set_theme()]


class App(Tk):
    def __init__(self):
        super().__init__()
        self.icon = PhotoImage(file="images/icon.png")
        self.iconphoto(False, self.icon)

        self.add_image = PhotoImage(file="images/add.png")
        self.more_img = PhotoImage(file="images/more.png")
        self.save_img = PhotoImage(file="images/save.png")
        self.load_img = PhotoImage(file="images/load.png")
        self.done_img = PhotoImage(file="images/done.png")
        self.new_img = PhotoImage(file="images/new.png")
        self.delete_img = PhotoImage(file="images/delete.png")
        self.apear_img = PhotoImage(file="images/apear.png")
        self.config(bg=theme["bg"])

        self.title("GoalKeeper")
        self.geometry("500x520")
        self.minsize(500, 520)

        self.text_font = ("Arial", 12, "bold")
        self.hint_font = ("Arial", 10, "bold")
        self.button_font = ("Arial", 7, "bold")
        self.tasks_num = 0
        self.steps_num = 0

        self.tasks_names = []
        self.tasks = {}

        # Goals frame

        self.frame = Frame(self, padx=5, bg=theme["menu"])
        self.frame.pack(side=LEFT, fill=BOTH)

        self.toolbar_frame = Frame(self.frame, bg=theme["segment"])
        self.toolbar_frame.pack(pady=3, fill=X)

        self.toolbar_hint = Label(self.toolbar_frame, font=self.hint_font, bg=theme["segment"], fg=theme["text-menu"])
        self.toolbar_hint.pack(side=RIGHT, padx=5)

        self.new_btn = Button(self.toolbar_frame, image=self.new_img, border=FALSE, highlightthickness=0,
                              cursor="hand2", activebackground=theme["segment"], bg=theme["segment"],
                              command=self.reset_app)
        self.new_btn.pack(side=LEFT, pady=2)
        self.new_btn.bind("<Enter>", lambda event: self.show_toolbar_hint("New"))
        self.new_btn.bind("<Leave>", lambda event: self.show_toolbar_hint(""))

        self.save_btn = Button(self.toolbar_frame, image=self.save_img, border=FALSE, highlightthickness=0,
                               cursor="hand2", activebackground=theme["segment"], bg=theme["segment"],
                               command=self.enter_save_name)
        self.save_btn.pack(side=LEFT, pady=2)
        self.save_btn.bind("<Enter>", lambda event: self.show_toolbar_hint("Save"))
        self.save_btn.bind("<Leave>", lambda event: self.show_toolbar_hint(""))

        self.load_btn = Button(self.toolbar_frame, image=self.load_img, border=FALSE, highlightthickness=0,
                               cursor="hand2", activebackground=theme["segment"], bg=theme["segment"],
                               command=self.open_load_window)
        self.load_btn.pack(side=LEFT, pady=2)
        self.load_btn.bind("<Enter>", lambda event: self.show_toolbar_hint("Load"))
        self.load_btn.bind("<Leave>", lambda event: self.show_toolbar_hint(""))

        self.appear_btn = Button(self.toolbar_frame, image=self.apear_img, border=FALSE, highlightthickness=0,
                                 cursor="hand2", activebackground=theme["segment"], bg=theme["segment"],
                                 command=self.open_appearance)
        self.appear_btn.pack(side=LEFT, pady=2)
        self.appear_btn.bind("<Enter>", lambda event: self.show_toolbar_hint("Appearance"))
        self.appear_btn.bind("<Leave>", lambda event: self.show_toolbar_hint(""))

        self.place_save_frame = Frame(self.frame, bg=theme["menu"])
        self.place_save_frame.pack(fill=X)

        self.save_frame = Frame(self.place_save_frame, bg=theme["segment"])

        self.save_hint = Label(self.save_frame, text="Save as", font=self.hint_font, bg=theme["segment"],
                               fg=theme["text-menu"])
        self.save_hint.pack()

        self.save_enter_name = Entry(self.save_frame, bg=theme["entry-menu"], fg=theme["entry-menu-text"], border=FALSE,
                                     width=25)
        self.save_enter_name.pack(side=LEFT, padx=5, pady=5)

        self.done_save = Button(self.save_frame, image=self.done_img, border=FALSE, highlightthickness=0,
                                cursor="hand2", activebackground=theme["segment"], command=self.save_book)
        self.done_save.pack(side=RIGHT, padx=5)

        self.place_load_frame = Frame(self.frame, bg=theme["menu"])
        self.place_load_frame.pack(fill=X)

        self.load_frame = Frame(self.place_load_frame, bg=theme["segment"])

        self.load_hint = Label(self.load_frame, text="Load", font=self.hint_font, bg=theme["segment"],
                               fg=theme["text-menu"])
        self.load_hint.pack()

        self.no_saves_label = Label(self.load_frame, text="No savings yet", font=self.hint_font, bg=theme["segment"],
                                    fg=theme["text-menu"])

        self.open_files_frame = Frame(self.load_frame, bg=theme["segment"])
        self.open_files_frame.pack(fill=X)

        self.close_load_btn = Button(self.load_frame, text="Close", font=self.button_font, bg=theme["button-bg"],
                                     fg=theme["button-text"], border=FALSE, cursor="hand2",
                                     command=self.close_load_window)

        self.input_frame = Frame(self.frame, bg=theme["segment"])
        self.input_frame.pack(pady=5, anchor=W)

        self.hint_label = Label(self.input_frame, text="Add a goal", fg=theme["text-menu"], bg=theme["segment"],
                                font=self.hint_font)
        self.hint_label.pack()

        self.add_categ = Button(self.input_frame, image=self.add_image, border=FALSE, cursor="hand2",
                                highlightthickness=0, activebackground=theme["segment"], command=self.new_goal)
        self.add_categ.pack(side=RIGHT, pady=5, padx=5)

        self.enter_name = Entry(self.input_frame, bg=theme["entry-menu"], fg=theme["entry-menu-text"], width=25,
                                border=FALSE)
        self.enter_name.pack(side=LEFT, pady=5, padx=5)

        self.goals_frame = Frame(self.frame, bg=theme["menu"])
        self.goals_frame.pack(fill=BOTH)

        # Description frame

        self.desc_frame = Frame(self, pady=5, bg=theme["bg"])
        self.desc_frame.pack(fill=X)

        self.task_name = Label(self.desc_frame, text="Welcome!", font=("Arial", 30, "bold"), bg=theme["bg"],
                               fg=theme["text-desc"])
        self.task_name.pack()

        self.input_step_frame = Frame(self.desc_frame, bg=theme["bg"])

        self.hint_desc = Label(self.input_step_frame, text="Add a step", font=self.hint_font, bg=theme["bg"],
                               fg=theme["text-desc"])
        self.hint_desc.pack(side=LEFT)

        self.add_step = Button(self.input_step_frame, image=self.add_image, border=FALSE, highlightthickness=0,
                               cursor="hand2", activebackground=theme["bg"], command=self.new_step)
        self.add_step.pack(side=RIGHT)

        self.input_step = Entry(self.input_step_frame, border=FALSE, bg=theme["entry-desc"],
                                fg=theme["entry-desc-text"])
        self.input_step.pack(fill=X, pady=5, padx=5)

        self.steps_list_frame = Frame(self.desc_frame, bg=theme["bg"])

    def new_goal(self) -> None:
        goal_name = self.enter_name.get().strip().capitalize()

        if goal_name != "" and goal_name not in self.tasks_names and self.tasks_num < 25:
            self.tasks_names.append(goal_name)
            self.tasks[goal_name] = []
            self.tasks[goal_name].append([])

            if len(goal_name) > 15:
                goal_name = goal_name[:16] + "..."
            goal_frame = Frame(self.goals_frame, bg=theme["menu"])
            goal_frame.pack(fill=X)

            goal = Label(goal_frame, text=goal_name, font=self.text_font, bg=theme["menu"], fg=theme["text-menu"])
            goal.pack(side=LEFT)

            check = Checkbutton(goal_frame, bg=theme["menu"], fg=theme["check-colour"], activebackground=theme["menu"],
                                cursor="hand2", border=FALSE)
            click = self.tasks_num
            more_btn = Button(goal_frame, text=str(self.tasks_num), image=self.more_img, border=FALSE,
                              highlightthickness=0, cursor="hand2", activebackground=theme["menu"], bg=theme["menu"],
                              command=lambda click=click: self.open_desc(click))

            check.pack(side=RIGHT)
            more_btn.pack(side=RIGHT)

            self.tasks_num += 1

    def new_step(self) -> None:
        step_name = self.input_step.get().strip()
        self.steps_num += 1

        if step_name != "":
            self.tasks[self.task_name["text"]].append(step_name)
            self.tasks[self.task_name["text"]][0].append(0)

            step_frame = Frame(self.steps_list_frame, bg=theme["bg"])
            step_frame.pack(fill=X, padx=5)

            check = Checkbutton(step_frame, bg=theme["bg"], activebackground=theme["bg"], fg=theme["check-colour"],
                                cursor="hand2", command=lambda i=self.steps_num: self.complete_step(i))
            check.pack(side=RIGHT)

            step_name = Label(step_frame, text=f"{self.steps_num}. {step_name}", bg=theme["bg"], fg=theme["text-desc"],
                              font=self.text_font)
            step_name.pack(side=LEFT)

    def open_desc(self, index: int) -> None:
        self.reset_steps()

        self.task_name["text"] = self.tasks_names[index]
        self.input_step_frame.pack(fill=X, padx=5)
        self.steps_list_frame.pack(fill=BOTH)

        task = self.tasks[self.task_name["text"]]
        self.steps_num = len(task[0])

        for i, step in enumerate(task):
            if i == 0:
                continue
            step_frame = Frame(self.steps_list_frame, bg=theme["bg"])
            step_frame.pack(fill=X, padx=5)

            check = Checkbutton(step_frame, bg=theme["bg"], activebackground=theme["bg"], fg=theme["check-colour"],
                                cursor="hand2", command=lambda i=i: self.complete_step(i))
            if task[0][i - 1]:
                check.select()

            check.pack(side=RIGHT)

            step = Label(step_frame, text=f"{i}. {step}", bg=theme["bg"], fg=theme["text-desc"], font=self.text_font)
            step.pack(side=LEFT)

    def complete_step(self, index: int) -> None:
        step_check = self.tasks[self.task_name["text"]][0][index - 1]
        step_check = 1 - step_check
        self.tasks[self.task_name["text"]][0][index - 1] = step_check

    def reset_steps(self) -> None:
        for step in self.steps_list_frame.winfo_children():
            step.destroy()
        self.steps_num = 0

    def show_toolbar_hint(self, text: str) -> None:
        self.toolbar_hint["text"] = text

    def enter_save_name(self) -> None:
        self.close_load_window()
        self.save_frame.pack(fill=X, anchor=W)

    def save_book(self) -> None:
        file_name = self.save_enter_name.get()
        if f"{file_name}.gk" in os.listdir("saves"):
            os.remove(f"saves/{file_name}.gk")

        def get_steps_names(arr):
            ret_str = ""
            for step in arr[1:]:
                ret_str += f"{step},"
            return ret_str

        def get_checks(arr):
            ret_str = ""
            for check in arr:
                ret_str += f"{check},"
            return ret_str

        if file_name.strip() != "":
            with open(f"saves/{file_name}.gk", "w", encoding="UTF-8") as save_file:
                for task in self.tasks:
                    save = f"{task}|{get_steps_names(self.tasks[task])}|{get_checks(self.tasks[task][0])}\n"
                    save_file.write(save)

        self.save_frame.pack_forget()
        self.place_save_frame.config(width=1, height=1)

    def open_load_window(self) -> None:

        def delete_file(name):
            os.remove(f"saves/{name}.gk")
            self.open_load_window()
            self.open_files_frame["height"] = 1

        self.close_load_btn.pack_forget()
        self.no_saves_label.pack_forget()

        for file in self.open_files_frame.winfo_children():
            file.destroy()
        names = [name[:-3] for name in os.listdir("saves") if name[-3:] == ".gk"]

        if len(names) == 0:
            self.no_saves_label.pack()

        for file in names:
            open_button = Frame(self.open_files_frame, bg=theme["segment"])
            open_button.pack(fill=X, padx=5)

            open_file = Button(open_button, text=file, font=self.button_font, bg=theme["button-bg"],
                               fg=theme["button-text"], border=FALSE, cursor="hand2",
                               command=lambda file=file: self.load_file(file))
            open_file.pack(side=LEFT, expand=TRUE, fill=X, pady=1)

            del_button = Button(open_button, image=self.delete_img, border=FALSE, highlightthickness=0, cursor="hand2",
                                activebackground=theme["segment"], command=lambda file=file: delete_file(file))
            del_button.pack(side=RIGHT, padx=2)

        self.save_frame.pack_forget()
        self.place_save_frame.config(width=1, height=1)
        self.load_frame.pack(fill=X, anchor=W)
        self.close_load_btn.pack(fill=X, padx=5, pady=5)

    def close_load_window(self) -> None:
        self.load_frame.pack_forget()
        self.place_load_frame.config(width=1, height=1)
        for file in self.open_files_frame.winfo_children():
            file.destroy()

    def load_file(self, name: str) -> None:
        self.reset_app()
        self.close_load_window()
        self.tasks = {}
        with open(f"saves/{name}.gk") as save_file:
            save = list(map(lambda x: x.strip(), save_file.readlines()))
            goal_names, goal_steps, goal_checks = [], [], []
            for goal in save:
                goal_names.append(goal.split("|")[0])
                goal_steps.append(goal.split("|")[1])
                goal_checks.append(goal.split("|")[2])

        for i, goal_name in enumerate(goal_names):
            self.tasks[goal_name] = [list(map(int, goal_checks[i][:-1].split(",")))]
            steps = goal_steps[i][:-1].split(",")
            for step in steps:
                self.tasks[goal_name].append(step)

        # create tasks
        for task in self.tasks:
            self.tasks_names.append(task)
            if len(task) > 15:
                task = task[:16] + "..."

            goal_frame = Frame(self.goals_frame, bg=theme["menu"])
            goal_frame.pack(fill=X)

            goal = Label(goal_frame, text=task, font=self.text_font, bg=theme["menu"], fg=theme["text-menu"])
            goal.pack(side=LEFT)

            check = Checkbutton(goal_frame, bg=theme["menu"], fg=theme["check-colour"], activebackground=theme["menu"],
                                cursor="hand2", border=FALSE)
            click = self.tasks_num
            more_btn = Button(goal_frame, text=str(self.tasks_num), image=self.more_img, border=FALSE,
                              highlightthickness=0, cursor="hand2", activebackground=theme["menu"], bg=theme["menu"],
                              command=lambda click=click: self.open_desc(click))

            check.pack(side=RIGHT)
            more_btn.pack(side=RIGHT)

            self.tasks_num += 1

    def reset_app(self) -> None:
        for goal in self.goals_frame.winfo_children():
            goal.destroy()

        for step in self.steps_list_frame.winfo_children():
            step.destroy()

        self.input_step_frame.pack_forget()
        self.steps_list_frame.pack_forget()
        self.steps_num = 0
        self.tasks_num = 0
        self.tasks_names = []

        self.task_name["text"] = "Welcome!"

    def open_appearance(self) -> None:
        apr_w.Appearance(theme)


if __name__ == "__main__":
    app = App()
    app.mainloop()
