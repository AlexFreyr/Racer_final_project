# coding=utf-8
"""
This is the file that should first executed by the user to make sure he is identified
"""
import tkinter
import cffi
from tkinter import ttk
from Login.login import Login
from Start.run import RunGame

LARGE_FONT = ("Verdana", 12)
MEDIUM_FONT = ("Verdana", 10)


class ClientApp(tkinter.Tk):
    """
    Contains all the pages that need to be set, in our case
    only 1 needs to be set but more could be added upon later
    """
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.container = tkinter.Frame(self)

        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(self.container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        """
        Shows the frame(window) that needs to be raised
        """
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tkinter.Frame):
    """
    The login window
    """
    def __init__(self, parent, controller):
        self.controller = controller
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Please log in", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        username_label = tkinter.Label(self, text="Enter your username here", font=MEDIUM_FONT)
        username_label.pack()
        username_entry = ttk.Entry(self)
        username_entry.pack()

        password_label = tkinter.Label(self, text="Enter your password here", font=MEDIUM_FONT)
        password_label.pack()
        password_entry = ttk.Entry(self, show="*")
        password_entry.pack()

        login_button = ttk.Button(self, text="Login",
                                  command=lambda: self.attempt_login(username_entry.get(), password_entry.get()))
        login_button.pack()

    def attempt_login(self, username, password):
        """
        When the user clicks login this attempts to login the user
        """
        login = Login()
        if login.login(username, password):
            self.destroy_window()
            r = RunGame(login.id, login.user, login.highscore)
            r.run_main()
        else:
            incorrect_text = tkinter.Label(self, text="Incorrect username/password", font=MEDIUM_FONT, fg="Red")
            incorrect_text.pack()

    def destroy_window(self):
        """
        Will execute if the user successfully logs in
        """
        self.destroy()
        app.destroy()

app = ClientApp()

app.title("Login form [Racer]")
app_width, app_height = 720, 240
screen_width, screen_height = app.winfo_screenwidth(), app.winfo_screenheight()
start_width, start_height = (screen_width / 2) - (app_width / 2), (screen_height / 2) - (app_height / 2)
app.geometry("%dx%d+%d+%d" % (app_width, app_height, start_width, start_height))


def on_closing():
    """
    If the window is closed before the user logs in this function is called
    """
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()
