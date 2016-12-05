# coding=utf-8
"""
This file contains the game itself
"""
import pygame
import random
import os
import time
from Menu.menu import Pause
from Text.text import Text
from Score.update import Update

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Run:
    """
    Class to run the game
    """
    def __init__(self, user_id, user, highscore, screen, display_width, display_height):
        self.user_id = user_id
        self.user = user
        self.highscore = highscore
        self.lastScore = 0
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.carImg = pygame.image.load(os.path.join('../src', 'blue_car.png'))
        self.carsImg = pygame.image.load(os.path.join('../src', 'cars.png'))
        self.background_img = pygame.image.load(os.path.join('../src', 'mainroad.png')).convert_alpha()
        self.background_pos = [0, 0]
        self.display_width = display_width
        self.display_height = display_height
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join('../Music', 'racer.mp3'))
        pygame.mixer.music.play(-1)
        self.run_game()

    def update_score(self, last_score, highscore):
        """
        Updates the highscore
        """
        self.lastScore = last_score
        self.highscore = highscore

        if highscore < last_score:
            u = Update()
            u.run_update(highscore, last_score, self.user_id)
            self.highscore = last_score

    def cars_dodged(self, count):
        """
        Displays to the user how many cars have been dodged
        """
        t = Text(self.screen)
        text_msg = " High Score: " + str(self.highscore) + " Score: " + str(count)
        t.draw_text_raw(text_msg, 110, 20, size=25, font_color=WHITE)

    def draw_car(self, car_x, car_y, car_width, car_height, car_color):
        """
        Draws the cars that go towards you
        """
        pygame.draw.rect(self.screen, car_color, [car_x, car_y, car_width, car_height])
        self.screen.blit(self.carsImg, (car_x - 15, car_y - 5))

    def user_car(self, x, y):
        """
        Draws the car the user controls
        """
        self.screen.blit(self.carImg, (x, y))

    def crash(self, last_score, highscore):
        """
        Will display the crash screen
        """
        t = Text(self.screen)
        respawn_timer = Text(self.screen)

        seconds = 0
        while seconds < 3:
            self.screen.fill(WHITE)
            t.draw_text_raw(str(self.user) + " you crashed!", self.display_width / 2, self.display_height / 2, 100)
            msg = str(3 - seconds) + " seconds until respawn"
            respawn_timer.draw_text_raw(msg, self.display_width / 2, self.display_height / 2.5)
            pygame.display.update()
            time.sleep(1)
            seconds += 1

        self.update_score(last_score, highscore)
        self.run_game()

    def run_game(self):
        """
        Game controls and the game itself
        """
        running = True
        clock = pygame.time.Clock()

        x = (self.display_width * 0.5)
        y = (self.display_height * 0.75)
        car_width = 94
        car_height = 214
        x_change = 0
        y_change = 0

        car1_start_x = random.randrange(0, self.display_width)
        car1_start_y = -600
        car1_speed = 4
        car1_width = 70
        car1_height = 190

        car2_start_x = random.randrange(0, self.display_width)
        car2_start_y = -800
        car2_width = 70
        car2_height = 190

        car3_start_x = random.randrange(0, self.display_width)
        car3_start_y = -1000
        car3_width = 70
        car3_height = 190

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
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                    if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                        y_change = 0
            x += x_change
            y += y_change
            self.screen.blit(self.background_img, self.background_pos)
            self.draw_car(car1_start_x, car1_start_y, car1_width, car1_height, BLACK)
            car1_start_y += car1_speed

            if dodged > 4:
                self.draw_car(car2_start_x, car2_start_y, car2_width, car2_height, BLACK)
                car2_start_y += car1_speed

            if dodged > 9:
                self.draw_car(car3_start_x, car3_start_y, car3_width, car3_height, BLACK)
                car3_start_y += car1_speed

            self.user_car(x, y)
            self.cars_dodged(dodged)

            if x > self.display_width - car_width or x < 0:
                self.crash(self.lastScore, self.highscore)
                self.lastScore = dodged

            if y > self.display_height - car_height or y < 0:
                self.lastScore = dodged
                self.crash(self.lastScore, self.highscore)

            if car1_start_y > self.display_height:
                car1_start_y = 0 - car1_height - 150
                car1_start_x = random.randrange(0, self.display_width - 200)
                dodged += 1
                car1_speed += 0.5

            if car2_start_y > self.display_height:
                car2_start_y = 0 - car2_height - 150
                car2_start_x = random.randrange(0, self.display_width - 200)
                dodged += 1
                car1_speed += 0.5

            if car3_start_y > self.display_height:
                car3_start_y = 0 - car3_height - 150
                car3_start_x = random.randrange(0, self.display_width - 200)
                dodged += 1
                car1_speed += 0.5

            if car1_start_x <= x <= car1_start_x + car1_width + 24 and y < car1_start_y + car1_height:
                self.lastScore = dodged
                self.crash(self.lastScore, self.highscore)

            if car1_start_x <= x + car_width <= car1_start_x + car1_width + 24 and y < car1_start_y + car1_height:
                self.lastScore = dodged
                self.crash(self.lastScore, self.highscore)

            if car2_start_x <= x <= car2_start_x + car2_width + 24 and y < car2_start_y + car2_height:
                self.lastScore = dodged
                self.crash(self.lastScore, self.highscore)

            if car2_start_x <= x + car_width <= car2_start_x + car2_width + 24 and y < car2_start_y + car2_height:
                self.lastScore = dodged
                self.crash(self.lastScore, self.highscore)

            if car3_start_x <= x <= car3_start_x + car3_width + 24 and y < car3_start_y + car3_height:
                self.lastScore = dodged
                self.crash(self.lastScore, self.highscore)

            if car3_start_x <= x + car_width <= car3_start_x + car3_width + 24 and y < car3_start_y + car3_height:
                self.lastScore = dodged
                self.crash(self.lastScore, self.highscore)

            pygame.display.update()
            clock.tick(60)
        pygame.quit()
        quit()
