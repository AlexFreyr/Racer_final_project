# coding=utf-8
"""
File contains classes to buttons that can be used
"""
import pygame
from Text.text import Text


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
