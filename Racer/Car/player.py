# coding=utf-8
"""
Used for the cars that will drive against the player
"""


class Player:
    """
    Initialize the player
    """
    def __init__(self, screen, x, y, width, height, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

        self.y_change = 0
        self.x_change = 0

    def draw_car(self):
        """
        Draws the player on the coordinates specified
        """
        self.x += self.x_change
        self.screen.blit(self.image, (self.x, self.y))

    def check_hit(self):
        """
        Checks if the player has hit either side of the window
        """
        if self.x > 1500 - self.width or self.x < 0:
            return True
