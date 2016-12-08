# coding=utf-8
"""
Build distribution file
"""
import random
import pygame
import pymysql
import pymysql.cursors
import bcrypt
import tkinter
import os
import time
from tkinter import ttk
from Login.login import Login
from main import RunGame

# coding=utf-8
"""
Controls the background and how it moves compared to the cars
"""


class Road:
    """
    Call this class when in need to make a background
    """
    def __init__(self, screen, road_img):
        self.screen = screen
        self.road_img = road_img

        self.x = 0
        self.y = 0

        self.x1 = 0
        self.y1 = -900

    def draw_road(self):
        """
        Draws the road and moves it accordingly
        """

        self.screen.blit(self.road_img, (self.x, self.y))
        self.screen.blit(self.road_img, (self.x1, self.y1))
        if self.y > 900:
            self.y = -900
        if self.y1 > 900:
            self.y1 = -900

# coding=utf-8
"""
File contains classes to buttons that can be used
"""


class SquareButton:
    """
    This button is a square button
    """
    def __init__(self, screen, x_pos, y_pos, width, height, color, hover_color, text):
        self.screen = screen
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_object = Text(screen)

    def draw_button(self):
        """
        Draws the button and controls the hover effect
        """
        pygame.draw.rect(self.screen, self.color, (self.x_pos, self.y_pos, self.width, self.height))
        if self.is_hover():
            pygame.draw.rect(self.screen, self.hover_color, (self.x_pos, self.y_pos, self.width, self.height))
        button_pos = self.get_position()
        self.text_object.draw_text(self.text, button_pos[0], button_pos[1], button_pos[2], button_pos[3])

    def get_position(self):
        """
        Returns four coordinates that represent the button (x, y, x1, y1)
        """
        return self.x_pos, self.x_pos + self.width, self.y_pos, self.y_pos + self.height

    def is_hover(self):
        """
        Checks if the button is being hovered on and returns true or false
        """
        button_pos = self.get_position()
        cursor_pos = pygame.mouse.get_pos()

        if button_pos[0] <= cursor_pos[0] <= button_pos[1] and button_pos[2] <= cursor_pos[1] <= button_pos[3]:
            return True
        else:
            return False

# coding=utf-8
"""
Used for the cars that will drive against the player
"""


class Car:
    """
    Initialize the car object
    """
    def __init__(self, screen, y, width, height, image, y_change=4):
        self.screen = screen
        self.x = random.randrange(0, 1500)
        self.y = y
        self.width = width
        self.height = height
        self.image = image

        self.y_change = y_change
        self.passed = False

    def draw_car(self):
        """
        Draws the car and resets its position when it goes off screen
        """
        self.y += self.y_change
        self.screen.blit(self.image, (self.x, self.y))

        if self.y > 900:
            self.passed = True
            self.y_change += 0.5
            self.y = 0 - self.height - 150
            self.x = random.randrange(0, 1500 - 200)

    def check_hit(self, user_x, user_y):
        """
        Checks if the player has hit the car and returns true if he has
        """
        if self.x <= user_x <= self.x + self.width and user_y < self.y + self.height:
            return True
        if self.x <= user_x + self.width <= self.x + self.width and user_y < self.y + self.height:
            return True

    def check_pass(self):
        """
        Returns true if the car has gone off screen
        """
        if self.passed:
            self.passed = False
            return True
        else:
            return False

# coding=utf-8
"""
Used for the cars that will drive against the player
"""


class Player:
    """
    Initialize the player
    """
    def __init__(self, screen, x, y, width, height, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

        self.y_change = 0
        self.x_change = 0

    def draw_car(self):
        """
        Draws the player on the coordinates specified
        """
        self.x += self.x_change
        self.screen.blit(self.image, (self.x, self.y))

    def check_hit(self):
        """
        Checks if the player has hit either side of the window
        """
        if self.x > 1500 - self.width or self.x < 0:
            return True


# coding=utf-8
"""
Login script that gets the user id, username and score from the database
"""


class Login:
    """
    Makes the connection to the database
    """
    def __init__(self):
        self.connection = pymysql.connect(host='vorur.info',
                                          user='developer',
                                          password='Vorur-dev123',
                                          db='racer',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.id = None
        self.user = None
        self.highscore = None

    def login(self, username, password):
        """
        This function returns true or false if the user enters
        the correct username and password to an account
        """
        with self.connection.cursor() as cursor:
            sql = "SELECT `id`,`username`,`password` FROM `racers` WHERE `username`=%s"
            cursor.execute(sql, username)
            result = cursor.fetchone()

            if result is not None:
                sql_highscore = "SELECT `score` FROM `scores` WHERE `racer_id`=%s"
                cursor.execute(sql_highscore, (result["id"]))
                highscore_result = cursor.fetchone()

                self.id = result["id"]
                self.user = result["username"]
                self.highscore = highscore_result["score"]
                self.connection.close()

                login_result = result['password'].encode('utf-8')
                if bcrypt.hashpw(password.encode('utf-8'), login_result) == login_result:
                    return True
        return False

# coding=utf-8
"""
This is the file that should first executed by the user to make sure he is identified
"""

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

# coding=utf-8
"""
Menu and pause that the user interacts with and has the ability to select different options
"""

# BACKGROUND_GREEN = (215, 255, 137)
# 111, 168, 0
BACKGROUND = (0, 0, 0)

# GLOBALS
fade_1 = True
fade_2 = True
fade_3 = True
WHITE = (255, 255, 255)
LIGHT_GREY = (207, 207, 207)


class Menu:
    """
    Initialize the menu when login is complete
    """
    def __init__(self, screen):
        self.screen = screen
        self.start_menu()

    @staticmethod
    def background_color(color1, color2):  # TODO: Fix the function to display the two colors fading in and out
        """
        Makes the background fade in and out of two colors
        """
        global fade_1, fade_2, fade_3

        if not fade_1 and not fade_2 and not fade_3:
            if color1[0] == 0:
                fade_1 = True
            else:
                color1[0] -= 1
        elif color1[0] <= color2[0] and fade_1:
            color1[0] += 1
            if color1[0] == color2[0]:
                fade_1 = False

        if not fade_1 and not fade_2 and not fade_3:
            if color1[1] == 0:
                fade_2 = True
            else:
                color1[1] -= 1
        elif color1[1] <= color2[1] and fade_2:
            color1[1] += 1
            if color1[1] == color2[1]:
                fade_2 = False

        if not fade_1 and not fade_2 and not fade_3 and fade_2 and fade_1:
            if color1[2] == 0:
                fade_3 = True
            else:
                color1[2] -= 1
        elif color1[2] <= color2[2] and fade_3:
            color1[2] += 1
            if color1[2] == color2[2]:
                fade_3 = False

        return color1[0], color1[1], color1[2]

    def start_menu(self):
        """
        This is the menu that controls the user actions
        """
        global BACKGROUND
        running = True
        clock = pygame.time.Clock()

        start_button = SquareButton(self.screen, 100, 200, 150, 50, WHITE, LIGHT_GREY, text_button_start)
        multiplayer_button = SquareButton(self.screen, 100, 300, 150, 50, WHITE, LIGHT_GREY, text_button_multiplayer)
        settings_button = SquareButton(self.screen, 100, 400, 150, 50, WHITE, LIGHT_GREY, text_button_settings)
        quit_button = SquareButton(self.screen, 100, 500, 150, 50, WHITE, LIGHT_GREY, text_button_exit)
        game_title_object = Text(self.screen)

        color1 = [111, 168, 0]
        color2 = [215, 255, 137]

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.is_hover():  # Quit menu
                        pygame.quit()
                        quit()
                    if start_button.is_hover():  # Start game
                        running = False
                    if settings_button.is_hover():
                        # Settings(self.screen)
                        pass

            BACKGROUND = self.background_color(color1, color2)
            self.screen.fill(BACKGROUND)

            game_title_object.draw_text_raw(text_game_title, 540, 100, 50)
            start_button.draw_button()
            multiplayer_button.draw_button()
            settings_button.draw_button()
            quit_button.draw_button()

            clock.tick(60)
            pygame.display.flip()
# coding=utf-8
"""
This allows you to customize the music playing
"""


class Music:
    """
    Class that controls multiple music effects such as volume and more
    """
    def __init__(self, music):
        pygame.mixer.init()
        pygame.mixer.music.load(music)
        self.music_volume = 95

    def volume(self, value):
        """
        :param value: Will adjust volume from 0 - 100
        """
        if 0 <= self.music_volume <= 100:
            if self.music_volume == 100:
                self.music_volume -= abs(value)
            elif self.music_volume == 0:
                self.music_volume += abs(value)
            else:
                self.music_volume += value
            pygame.mixer.music.set_volume(self.music_volume / 100)
        print(self.music_volume)

    @staticmethod
    def play(loop=-1):
        """
        Start playing the music
        :loop can be set to loop every x second default is -1 which will loop forever
        """
        pygame.mixer.music.play(loop)

    @staticmethod
    def stop():
        """
        Stops playing the music
        """
        pygame.mixer.music.stop()


class Pause:
    """
    Pause menu that is called when the user pauses the game
    """
    def __init__(self, screen):
        self.screen = screen
        self.pause_menu()

    def pause_menu(self):
        """
        This is the pause menu that controls the user actions
        """
        running = True

        screen_title = Text(self.screen)
        unpause_button = SquareButton(self.screen, 100, 200, 150, 50, WHITE, LIGHT_GREY, text_button_stop_pause)
        settings_button = SquareButton(self.screen, 100, 300, 150, 50, WHITE, LIGHT_GREY, text_button_settings)
        back_to_menu = SquareButton(self.screen, 100, 400, 150, 50, WHITE, LIGHT_GREY, text_button_back_to_menu)
        quit_button = SquareButton(self.screen, 100, 500, 150, 50, WHITE, LIGHT_GREY, text_button_exit)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if unpause_button.is_hover():
                        running = False
                    if settings_button.is_hover():
                        Settings(self.screen)
                    if back_to_menu.is_hover():
                        Menu(self.screen)
                    if quit_button.is_hover():
                        pygame.quit()
                        quit()

            screen_title.draw_text_raw(text_game_paused, 540, 100, 50, font_color=WHITE)
            unpause_button.draw_button()
            settings_button.draw_button()
            back_to_menu.draw_button()
            quit_button.draw_button()

            pygame.display.update()

# coding=utf-8
"""
Updates the user score with the highscore that the user gets
"""


class Update:
    """
    Update class that sets the connection to the database
    """
    def __init__(self):
        self.connection = pymysql.connect(host='vorur.info',
                                          user='developer',
                                          password='Vorur-dev123',
                                          db='racer',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def run_update(self, highscore, last_score, user_id):
        """
        Update the information with a update query to the database
        """
        if last_score > highscore:
            with self.connection.cursor() as cursor:
                update_score = "UPDATE `scores` SET `score`=%s WHERE `racer_id`=%s"
                cursor.execute(update_score, (last_score, user_id))
                cursor.close()
                self.connection.commit()
                self.connection.close()
                print("Score updated")

# coding=utf-8
"""
Settings menu that is not used for now but could be used to control sound and more
"""

WHITE = (255, 255, 255)
LIGHT_GREY = (207, 207, 207)


class Settings:
    """
    Settings menu that is called when the user chooses it from a menu
    """
    def __init__(self, screen):
        self.screen = screen
        self.start_settings()

    def start_settings(self):
        """
        This is the settings menu that controls the user actions
        """
        screen_title = Text(self.screen)
        back = SquareButton(self.screen, 100, 200, 150, 50, WHITE, LIGHT_GREY, text_button_back)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back.is_hover():  # Quit settings
                        running = False

            self.screen.fill(WHITE)

            screen_title.draw_text_raw(text_button_settings, 540, 100, 50)
            back.draw_button()

            pygame.display.update()

# coding=utf-8
"""
This file contains the game itself
"""

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Run:
    """
    Class to run the game
    """
    def __init__(self, user_id, user, highscore, screen, display_width, display_height):
        self.user_id = user_id
        self.user = user
        self.highscore = highscore
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.carImg = pygame.image.load(os.path.join('src', 'blue_car.png'))
        self.carsImg = pygame.image.load(os.path.join('src', 'cars.png'))
        self.road_img = pygame.image.load(os.path.join('src', 'mainroad.png')).convert_alpha()
        self.display_width = display_width
        self.display_height = display_height

        self.music = Music("Music/racer.mp3")
        self.music.play()

        self.run_game()

    def update_score(self, last_score, highscore):
        """
        Updates the highscore
        """

        if highscore < last_score:
            u = Update()
            u.run_update(highscore, last_score, self.user_id)
            self.highscore = last_score

    def cars_dodged(self, count):
        """
        Displays to the user how many cars have been dodged
        """
        t = Text(self.screen)
        text_msg = " High Score: " + str(self.highscore) + " Score: " + str(count)
        t.draw_text_raw(text_msg, 120, 20, size=25, font_color=WHITE)

    def crash(self, last_score, highscore):
        """
        Will display the crash screen for 3 seconds
        """
        t = Text(self.screen)
        respawn_timer = Text(self.screen)
        self.update_score(last_score, highscore)

        seconds = 0
        while seconds < 3:
            self.screen.fill(WHITE)
            msg = str(3 - seconds) + " seconds until respawn"

            t.draw_text_raw(str(self.user) + " you crashed!", self.display_width / 2, self.display_height / 2, 100)
            respawn_timer.draw_text_raw(msg, self.display_width / 2, self.display_height / 2.5)

            pygame.display.update()
            time.sleep(1)
            seconds += 1

        self.run_game()

    def run_game(self):
        """
        Game controls and the game itself
        """
        running = True

        clock = pygame.time.Clock()
        x = (self.display_width * 0.5)
        y = (self.display_height * 0.75)
        player = Player(self.screen, x, y, 94, 214, self.carImg)
        car_list = [Car(self.screen, -600, 70, 190, self.carsImg)]
        road = Road(self.screen, self.road_img)

        dodged = 0
        dodged_4 = False
        dodged_9 = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Pause(self.screen)
                    if event.key == pygame.K_LEFT:
                        player.x_change = -10
                    if event.key == pygame.K_RIGHT:
                        player.x_change = 10
                    if event.key == pygame.K_KP_MINUS:
                        self.music.volume(-5)
                    if event.key == pygame.K_KP_PLUS:
                        self.music.volume(5)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player.x_change = 0

            # Draw the road and move it with the cars
            road.draw_road()
            road.y1 += car_list[0].y_change
            road.y += car_list[0].y_change

            # Draw the player
            player.draw_car()
            if player.check_hit():
                self.crash(dodged, self.highscore)

            # Add one car if dodge is equal to 4 or 9
            if dodged == 4 and not dodged_4:
                dodged_4 = True
                car_list.append(Car(self.screen, -800, 70, 190, self.carsImg, car_list[0].y_change))
            if dodged == 9 and not dodged_9:
                dodged_9 = True
                car_list.append(Car(self.screen, -1000, 70, 190, self.carsImg, car_list[0].y_change))

            # Draw all the cars
            for car in car_list:
                if car.check_pass():
                    dodged += 1
                car.draw_car()
                if car.check_hit(player.x, player.y):
                    self.crash(dodged, self.highscore)

            # Display the numbers of cars dodged
            self.cars_dodged(dodged)

            pygame.display.update()
            clock.tick(60)
        pygame.quit()
        quit()

# coding=utf-8
"""
Game text that can be edited.
This makes it easier to locate certain key actions or dialogue and change it if needed
"""
# Game menu's
text_game_title = "Racer game"
text_game_caption = "Racer"
text_game_paused = "Paused"
text_button_exit = "Exit"
text_button_stop_pause = "Resume"
text_button_start = "Start"
text_button_settings = "Settings"
text_button_multiplayer = "Multiplayer"
text_button_back = "Back"
text_button_back_to_menu = "Return to menu"

# coding=utf-8
"""
Text display
"""

BLACK = (0, 0, 0)


class Text:
    """
    Class for text display on the pygame screen
    """
    def __init__(self, screen):
        self.screen = screen

    @staticmethod
    def text_objects(text, font, font_color):
        """
        Should only be used by the Text class and shouldn't be edited
        """
        text_surface = font.render(text, True, font_color)
        return text_surface, text_surface.get_rect()

    def draw_text(self, text, x, y, x1, y1, size=20, font="Calibri", font_color=BLACK):
        """
        Draw text around four coordinates, useful for displaying text on a button
        """
        font_use = pygame.font.SysFont(font, size)
        text_surf, text_rect = self.text_objects(text, font_use, font_color)
        text_rect.center = ((x / 2 + (y / 2)), (x1 / 2 + (y1 / 2)))
        self.screen.blit(text_surf, text_rect)

    def draw_text_raw(self, text, x, y, size=20, font="Calibri", font_color=BLACK):
        """
        Draw text from two coordinates, useful for displaying text on screen normally
        """
        font_use = pygame.font.SysFont(font, size)
        text_surf, text_rect = self.text_objects(text, font_use, font_color)
        text_rect.center = x, y
        self.screen.blit(text_surf, text_rect)








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
