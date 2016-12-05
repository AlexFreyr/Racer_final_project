# coding=utf-8
"""
Text display
"""
import pygame

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
