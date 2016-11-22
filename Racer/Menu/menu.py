import pygame

from Buttons.button import SquareButton
from Settings.settings import Settings
from Text.game_text import *
from Text.text import Text
from Menu.popup import Popup

# BACKGROUND_GREEN = (215, 255, 137)
# 111, 168, 0
BACKGROUND = (0, 0, 0)

# GLOBALS
fade_1 = True
fade_2 = True
fade_3 = True
WHITE = (255, 255, 255)
LIGHT_GREY = (207, 207, 207)


class Menu:  # Menu class for when the game starts
    def __init__(self, screen):
        self.screen = screen
        self.start_menu()

    @staticmethod
    def background_color(color1, color2):  # TODO: Fix the function to display the two colors fading in and out
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

        # print(color1)
        # print(color2)

        return color1[0], color1[1], color1[2]

    def start_menu(self):
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
                        #Settings(self.screen)
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


class Pause:  # Pause class for when the game is paused
    def __init__(self, screen):
        self.screen = screen
        self.pause_menu()

    def pause_menu(self):
        running = True

        unpause_button = SquareButton(self.screen, 100, 200, 150, 50, WHITE, LIGHT_GREY, text_button_stop_pause)
        settings_button = SquareButton(self.screen, 100, 300, 150, 50, WHITE, LIGHT_GREY, text_button_settings)
        back_to_menu = SquareButton(self.screen, 100, 400, 150, 50, WHITE, LIGHT_GREY, text_button_back_to_menu)
        quit_button = SquareButton(self.screen, 100, 500, 150, 50, WHITE, LIGHT_GREY, text_button_exit)
        quit_popup = Popup(self.screen)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if unpause_button.is_hover():
                        running = False
                    if settings_button.is_hover():
                        Settings(self.screen)
                    if back_to_menu.is_hover():
                        Menu(self.screen)
                    if quit_button.is_hover():
                        quit_popup.yes_no_popup("Are you sure you want to quit?")
                        pygame.quit()
                        quit()

            unpause_button.draw_button()
            settings_button.draw_button()
            back_to_menu.draw_button()
            quit_button.draw_button()

            pygame.display.flip()
