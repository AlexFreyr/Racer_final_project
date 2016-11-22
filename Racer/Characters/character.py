import pygame


class Player:
    def __init__(self, screen, image, x=0, y=0):
        self.screen = screen
        self.image = image
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

    def draw_player(self):
        self.x += self.x_change
        self.y += self.y_change

        self.screen.blit(self.image, (self.x, self.y))
