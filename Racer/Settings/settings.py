# coding=utf-8
"""
Settings menu that is not used for now but could be used to control sound and more
"""
import pygame

RED = (255, 0, 0)


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
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.fill(RED)

            pygame.display.flip()
