# coding=utf-8
"""
Settings menu that is not used for now but could be used to control sound and more
"""
import pygame
from Text.game_text import *
from Buttons.button import SquareButton
from Text.text import Text

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
