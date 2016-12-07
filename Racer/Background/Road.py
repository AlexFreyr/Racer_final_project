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
        self.background_rect = self.road_img.get_rect()

        self.x = 0
        self.y = 0

        self.x1 = 0
        self.y1 = -900

    def draw_road(self):
        """
        Draws the road and moves it accordingly
        """
        self.screen.blit(self.road_img, self.background_rect)

        self.screen.blit(self.road_img, (self.x, self.y))
        self.screen.blit(self.road_img, (self.x1, self.y1))
        if self.y > 900:
            self.y = -900
        if self.y1 > 900:
            self.y1 = -900
