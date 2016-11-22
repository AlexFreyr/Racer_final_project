import pygame
import random
import os
import time
from Menu.menu import Pause
from Text.text import Text

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Run:
    def __init__(self, screen, display_width, display_height):
        self.screen = screen
        self.clock = pygame.time.Clock()
        # Alex: I can't load the images without having the full path ?
        self.carImg = pygame.image.load(os.path.join('C:\\Users\\Notandi\\Desktop\\Racer-python\\src', 'blue_car.png'))
        self.carsImg = pygame.image.load(os.path.join('C:\\Users\\Notandi\\Desktop\\Racer-python\\src', 'cars.png'))
        self.display_width = display_width
        self.display_height = display_height
        self.run_game()

    def cars(self, carsX, carsY):
        self.screen.blit(self.carsImg, (carsX, carsY))

    def things_dodged(self, count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: " + str(count), True, BLACK)
        self.screen.blit(text, (0, 0))

    def things(self, thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(self.screen, color, [thingx, thingy, thingw, thingh])
        self.screen.blit(self.carsImg, (thingx - 25, thingy - 50))

    def car(self, x, y):
        self.screen.blit(self.carImg, (x, y))

    def crash(self):
        t = Text(self.screen)
        respawn_timer = Text(self.screen)

        seconds = 0
        while seconds < 3:
            self.screen.fill(WHITE)
            t.draw_text_raw("You crashed!", self.display_width / 2, self.display_height / 2, 100)
            respawn_timer.draw_text_raw(str(3 - seconds) + " seconds until respawn", self.display_width / 2, self.display_height / 2.5)
            pygame.display.update()
            time.sleep(1)
            seconds += 1

        self.run_game()

    def run_game(self):
        running = True
        clock = pygame.time.Clock()

        x = (self.display_width * 0.5)
        y = (self.display_height * 0.5)
        car_width = 170
        car_height = 300
        x_change = 0
        y_change = 0

        thing_startx = random.randrange(0, self.display_width)
        thing_starty = -600
        thing_speed = 4
        thing_width = 120
        thing_height = 230
        dodged = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Pause(self.screen)
                    if event.key == pygame.K_LEFT:
                        x_change = -10
                    if event.key == pygame.K_RIGHT:
                        x_change = 10
                    if event.key == pygame.K_UP:
                        y_change = -5
                    if event.key == pygame.K_DOWN:
                        y_change = 10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        y_change = 0
            x += x_change
            y += y_change
            self.screen.fill(WHITE)
            self.things(thing_startx, thing_starty, thing_width, thing_height, BLACK)
            thing_starty += thing_speed
            self.car(x, y)
            self.things_dodged(dodged)

            if x > self.display_width - car_width or x < 0:
                self.crash()

            if y > self.display_height - car_height or y < 0: # Endless crash loop
                self.crash()

            if thing_starty > self.display_height:
                thing_starty = 0 - thing_height - 150
                thing_startx = random.randrange(0, self.display_width - 200)
                dodged += 1
                thing_speed += 1

            if y < thing_starty + thing_height:
                print('y crossover')

                if thing_startx <= x <= thing_startx + thing_width or thing_startx < x + car_width < thing_startx + thing_width:
                    print('X crossover')
                    self.crash()

            pygame.display.update()
            clock.tick(60)
        pygame.quit()
        quit()