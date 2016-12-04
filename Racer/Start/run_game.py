import pygame
import random
import os
import time
from Menu.menu import Pause
from Text.text import Text
from UpdateScore.ScoreUpdate import runupdate
from Login.login import Login




BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Run:
    def __init__(self,user_id, user, highscore, screen, display_width, display_height):
        self.user_id = user_id
        self.user = user
        self.highscore = highscore
        self.lastScore = 0
        self.screen = screen
        self.clock = pygame.time.Clock()
        # Alex: I can't load the images without having the full path ?
        self.carImg = pygame.image.load(os.path.join('C:\\Users\\Remi\\Desktop\\Racer\\src', 'blue_car.png'))
        self.carsImg = pygame.image.load(os.path.join('C:\\Users\\Remi\\Desktop\\Racer\\src', 'cars.png'))
        self.backgroundimg = pygame.image.load(os.path.join('C:\\Users\\Remi\\Desktop\\Racer\\src', 'Road.jpg'))
        self.backgroundpossition = [0, 0]
        self.display_width = display_width
        self.display_height = display_height
        pygame.mixer.init()
        pygame.mixer.music.load('C:\\Users\\Remi\\Desktop\\Racer\\Music\\razersoundtrack.mp3')
        self.run_game()

    def updateScore(self, lastscore, highscore, user_id):
        self.lastScore = lastscore
        self.highscore = highscore
        self.user_id = user_id

        print(user_id)
        print(lastscore)
        print(highscore)

        if highscore < lastscore:
            runupdate(highscore, lastscore, user_id)

        else:
            print("No new high score")

    def cars(self, carsX, carsY):
        self.screen.blit(self.carsImg, (carsX, carsY))

    def things_dodged(self, count):
        font = pygame.font.SysFont(None, 25)
        text = font.render(str(self.user) + " High Score: " + str(self.highscore) + " Score: " + str(count), True, WHITE)
        self.screen.blit(text, (0, 0))

    def things(self, thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(self.screen, color, [thingx, thingy, thingw, thingh])
        self.screen.blit(self.carsImg, (thingx -15, thingy -5))

    def things2(self, thing2x, thing2y, thing2w, thing2h, color2):
        pygame.draw.rect(self.screen, color2, [thing2x, thing2y, thing2w, thing2h])
        self.screen.blit(self.carsImg, (thing2x -15, thing2y -5))

    def things3(self, thing3x, thing3y, thing3w, thing3h, color3):
        pygame.draw.rect(self.screen, color3, [thing3x, thing3y, thing3w, thing3h])
        self.screen.blit(self.carsImg, (thing3x - 15, thing3y - 5))

    def car(self, x, y):
        self.screen.blit(self.carImg, (x, y))

    def crash(self):
        t = Text(self.screen)
        respawn_timer = Text(self.screen)

        seconds = 0
        while seconds < 3:
            self.screen.fill(WHITE)
            t.draw_text_raw(str(self.user) + " you crashed!", self.display_width / 2, self.display_height / 2, 100)
            respawn_timer.draw_text_raw(str(3 - seconds) + " seconds until respawn", self.display_width / 2, self.display_height / 2.5)
            pygame.display.update()
            time.sleep(1)
            seconds += 1

        self.run_game()

    def run_game(self):
        pygame.mixer.music.play(-1)
        running = True
        clock = pygame.time.Clock()

        x = (self.display_width * 0.5)
        y = (self.display_height * 0.75)
        car_width = 94
        car_height = 214
        x_change = 0
        y_change = 0

        thing_startx = random.randrange(0, self.display_width)
        thing_starty = -600
        thing_speed = 4
        thing_width = 70
        thing_height = 190

        thing2_startx = random.randrange(0, self.display_width)
        thing2_starty = -800
        thing2_width = 70
        thing2_height = 190

        thing3_startx = random.randrange(0, self.display_width)
        thing3_starty = -1000
        thing3_width = 70
        thing3_height = 190

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
            self.screen.blit(self.backgroundimg, self.backgroundpossition)
            self.things(thing_startx, thing_starty, thing_width, thing_height, BLACK)
            thing_starty += thing_speed

            if dodged > 4:
                self.things2(thing2_startx, thing2_starty, thing2_width, thing2_height, BLACK)
                thing2_starty += thing_speed

            if dodged > 9:
                self.things3(thing3_startx, thing3_starty, thing3_width, thing3_height, BLACK)
                thing3_starty += thing_speed

            self.car(x, y)
            self.things_dodged(dodged)

            if x > self.display_width - car_width or x < 0:
                self.crash()
                self.lastScore = dodged

            if y > self.display_height - car_height or y < 0: # Endless crash loop
                self.lastScore = dodged
                self.crash()

            if thing_starty > self.display_height:
                thing_starty = 0 - thing_height - 150
                thing_startx = random.randrange(0, self.display_width - 200)
                dodged += 1
                thing_speed += 0.5

            if thing2_starty > self.display_height:
                thing2_starty = 0 - thing2_height - 150
                thing2_startx = random.randrange(0, self.display_width - 200)
                dodged += 1
                thing_speed += 0.5

            if thing3_starty > self.display_height:
                thing3_starty = 0 - thing3_height - 150
                thing3_startx = random.randrange(0, self.display_width - 200)
                dodged += 1
                thing_speed += 0.5

            if x >= thing_startx and x <= thing_startx + thing_width + 24 and y < thing_starty + thing_height:
                self.lastScore = dodged
                self.crash()

            if x + car_width >= thing_startx and x + car_width <= thing_startx + thing_width + 24 and y < thing_starty + thing_height:
                self.lastScore = dodged
                self.crash()

            if x >= thing2_startx and x <= thing2_startx + thing2_width + 24 and y < thing2_starty + thing2_height:
                self.lastScore = dodged
                self.crash()

            if x + car_width >= thing2_startx and x + car_width <= thing2_startx + thing2_width + 24 and y < thing2_starty + thing2_height:
                self.lastScore = dodged
                self.crash()

            if x >= thing3_startx and x <= thing3_startx + thing3_width + 24 and y < thing3_starty + thing3_height:
                self.lastScore = dodged
                self.crash()

            if x + car_width >= thing3_startx and x + car_width <= thing3_startx + thing3_width + 24 and y < thing3_starty + thing3_height:
                self.lastScore = dodged
                self.crash()

            pygame.display.update()
            clock.tick(144)
        pygame.quit()
        quit()