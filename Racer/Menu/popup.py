import pygame
from Text.text import Text
from Buttons.button import SquareButton

WHITE = (255, 255, 255)
LIGHT_GREY = (207, 207, 207)


class Popup:
    def __init__(self, screen):
        self.screen = screen

    def yes_no_popup(self, custom_text):
        running = True
        dialog = Text(self.screen)
        yes_button = SquareButton(self.screen, 440, 300, 100, 75, WHITE, LIGHT_GREY, "Yes")

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.draw.rect(self.screen, WHITE, (365, 285, 350, 150))
            dialog.draw_text_raw(custom_text, 200, 250)
            yes_button.draw_button()

            pygame.display.flip()
