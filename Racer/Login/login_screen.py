import tkinter as tk
from tkinter import ttk
from Login.login import Login
from main import RunGame

LARGE_FONT = ("Verdana", 12)
MEDIUM_FONT = ("Verdana", 10)


class ClientApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)

        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(self.container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Please log in", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        username_label = tk.Label(self, text="Enter your username here", font=MEDIUM_FONT)
        username_label.pack()
        username_entry = ttk.Entry(self)
        username_entry.pack()

        password_label = tk.Label(self, text="Enter your password here", font=MEDIUM_FONT)
        password_label.pack()
        password_entry = ttk.Entry(self, show="*")
        password_entry.pack()

        login_button = ttk.Button(self, text="Login",
                                  command=lambda: self.attempt_login(username_entry.get(), password_entry.get()))
        login_button.pack()

    def attempt_login(self, username, password):
        login = Login()
        if login.login(username, password):
            self.destroy_window()
            r = RunGame(login.id, login.user, login.highscore)
            r.run_main()
        else:
            incorrect_text = tk.Label(self, text="Incorrect username/password", font=MEDIUM_FONT, fg="Red")
            incorrect_text.pack()

    def destroy_window(self):
        self.destroy()
        app.destroy()

app = ClientApp()

app.title("Login form [Racer]")
app_width, app_height = 720, 240
screen_width, screen_height = app.winfo_screenwidth(), app.winfo_screenheight()
start_width, start_height = (screen_width / 2) - (app_width / 2), (screen_height / 2) - (app_height / 2)
app.geometry("%dx%d+%d+%d" % (app_width, app_height, start_width, start_height))


def on_closing():
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()