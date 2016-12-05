# coding=utf-8
"""
Used for the cars that will drive against the player
"""
import random


class Car:
    """
    Initialize the car object
    """
    def __init__(self, screen, y, width, height, image, y_change=4):
        self.screen = screen
        self.x = random.randrange(0, 1500)
        self.y = y
        self.width = width
        self.height = height
        self.image = image

        self.y_change = y_change
        self.passed = False

    def draw_car(self):
        """
        Draws the car and resets its position when it goes off screen
        """
        self.y += self.y_change
        self.screen.blit(self.image, (self.x, self.y))

        if self.y > 900:
            self.passed = True
            self.y_change += 0.5
            self.y = 0 - self.height - 150
            self.x = random.randrange(0, 1500 - 200)

    def check_hit(self, user_x, user_y):
        """
        Checks if the player has hit the car and returns true if he has
        """
        if self.x <= user_x <= self.x + self.width and user_y < self.y + self.height:
            return True
        if self.x <= user_x + self.width <= self.x + self.width and user_y < self.y + self.height:
            return True

    def check_pass(self):
        """
        Returns true if the car has gone off screen
        """
        if self.passed:
            self.passed = False
            return True
        else:
            return False
