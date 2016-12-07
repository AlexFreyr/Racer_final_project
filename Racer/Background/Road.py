# coding=utf-8
"""
Controls the background and how it moves compared to the cars
"""
import pygame


class Road:
    """
    Call this class when in need to make a background
    """
    def __init__(self, screen, road_img):
        self.screen = screen
        self.road_img = pygame.image.load(road_img).convert_alpha()

        self.x = 0
        self.y = 0
        self.x_change = 0
        self.y_change = 0

    def draw_road(self):
        """
        Draws the road and moves it accordingly
        """
        if self.y >= 100:
            self.y = 0

        self.x += self.x_change
        self.y += self.y_change

        self.screen.blit(self.road_img, (self.x, self.y))