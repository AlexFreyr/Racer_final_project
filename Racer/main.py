import os
import pygame
from Menu.menu import Menu
from Start.run_game import Run
from Text.game_text import text_game_caption

pygame.init()


class RunGame:
    def __init__(self, user_id):
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.user_id = user_id
        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption(text_game_caption)

    def run_main(self):
        clock = pygame.time.Clock()  # TODO: Fix time step
        Menu(self.screen)
        Run(self.screen, 1080, 720)

        clock.tick(60)  # Use for later reference

RunGame(1).run_main()# TODO: REMOVE THIS LINE WHEN TESTING IS COMPLETE, THIS LINE PREVENTS THE LOGIN SCREEN FROM SHOWING