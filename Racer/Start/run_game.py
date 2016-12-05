# coding=utf-8
"""
This file contains the game itself
"""
import pygame
import os
import time
from Menu.menu import Pause
from Text.text import Text
from Score.update import Update
from Car.car import Car
from Car.player import Player

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
        t.draw_text_raw(text_msg, 120, 20, size=25, font_color=WHITE)

    def crash(self, last_score, highscore):
        """
        Will display the crash screen for 3 seconds
        """
        t = Text(self.screen)
        respawn_timer = Text(self.screen)
        self.update_score(last_score, highscore)

        seconds = 0
        while seconds < 3:
            self.screen.fill(WHITE)
            msg = str(3 - seconds) + " seconds until respawn"

            t.draw_text_raw(str(self.user) + " you crashed!", self.display_width / 2, self.display_height / 2, 100)
            respawn_timer.draw_text_raw(msg, self.display_width / 2, self.display_height / 2.5)

            pygame.display.update()
            time.sleep(1)
            seconds += 1

        self.run_game()

    def run_game(self):
        """
        Game controls and the game itself
        """
        running = True
        clock = pygame.time.Clock()

        x = (self.display_width * 0.5)
        y = (self.display_height * 0.75)
        player = Player(self.screen, x, y, 94, 214, self.carImg)
        car_list = [Car(self.screen, -600, 70, 190, self.carsImg)]

        dodged = 0
        dodged_4 = False
        dodged_9 = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Pause(self.screen)
                    if event.key == pygame.K_LEFT:
                        player.x_change = -10
                    if event.key == pygame.K_RIGHT:
                        player.x_change = 10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player.x_change = 0
            self.screen.blit(self.background_img, self.background_pos)

            # Draw the player
            player.draw_car()
            if player.check_hit():
                self.crash(dodged, self.highscore)

            # Add one car if dodge is equal to 4 or 9
            if dodged == 4 and not dodged_4:
                dodged_4 = True
                car_list.append(Car(self.screen, -800, 70, 190, self.carsImg, car_list[0].y_change))
            if dodged == 9 and not dodged_9:
                dodged_9 = True
                car_list.append(Car(self.screen, -1000, 70, 190, self.carsImg, car_list[0].y_change))

            # Draw all the cars
            for car in car_list:
                if car.check_pass():
                    dodged += 1
                car.draw_car()
                if car.check_hit(player.x, player.y):
                    self.crash(dodged, self.highscore)

            # Display the numbers of cars dodged
            self.cars_dodged(dodged)

            pygame.display.update()
            clock.tick(60)
        pygame.quit()
        quit()
