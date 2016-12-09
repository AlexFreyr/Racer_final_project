# coding=utf-8
"""
Sets the pygame window
is called from login_screen.py
"""
import os
import pygame
from Menu.menu import Menu
from Start.run_game import Run
from Text.game_text import text_game_caption

pygame.init()


class RunGame:
    """
    Class that contains all the window default settings
    """
    def __init__(self, user_id, user, highscore):
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.user_id = user_id
        self.user = user
        self.highscore = highscore
        self.screen = pygame.display.set_mode((1500, 900))
        pygame.display.set_caption(text_game_caption)

    def run_main(self):
        """
        Runs the menu and then the game based on what the user does in the menu
        """
        clock = pygame.time.Clock()  # TODO: Fix time step
        Menu(self.screen)
        Run(self.user_id, self.user, self.highscore, self.screen, 1500, 900)

        clock.tick(60)  # Use for later reference