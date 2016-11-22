import pygame

BLACK = (0, 0, 0)


class Text:
    def __init__(self, screen):
        self.screen = screen

    @staticmethod
    def text_objects(text, font, font_color):
        text_surface = font.render(text, True, font_color)
        return text_surface, text_surface.get_rect()

    def draw_text(self, text, x, y, x1, y1, size=20, font="Calibri", font_color=BLACK):
        font_use = pygame.font.SysFont(font, size)
        text_surf, text_rect = self.text_objects(text, font_use, font_color)
        text_rect.center = ((x / 2 + (y / 2)), (x1 / 2 + (y1 / 2)))
        self.screen.blit(text_surf, text_rect)

    def draw_text_raw(self, text, x, y, size=20, font="Calibri", font_color=BLACK):
        font_use = pygame.font.SysFont(font, size)
        text_surf, text_rect = self.text_objects(text, font_use, font_color)
        text_rect.center = x, y
        self.screen.blit(text_surf, text_rect)
