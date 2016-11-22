import pygame

RED = (255, 0, 0)


class Settings:
    def __init__(self, screen):
        self.screen = screen
        self.start_settings()

    def start_settings(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.fill(RED)

            pygame.display.flip()
