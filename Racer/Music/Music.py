# coding=utf-8
"""
This allows you to customize the music playing
"""
import pygame


class Music:
    """
    Class that controls multiple music effects such as volume and more
    """
    def __init__(self, music):
        pygame.mixer.init()
        pygame.mixer.music.load(music)
        self.music_volume = 95

    def volume(self, value):
        """
        :param value: Will adjust volume from 0 - 100
        """
        if 0 <= self.music_volume <= 100:
            if self.music_volume == 100:
                self.music_volume -= abs(value)
            elif self.music_volume == 0:
                self.music_volume += abs(value)
            else:
                self.music_volume += value
            pygame.mixer.music.set_volume(self.music_volume / 100)
        print(self.music_volume)

    @staticmethod
    def play(loop=-1):
        """
        Start playing the music
        :loop can be set to loop every x second default is -1 which will loop forever
        """
        pygame.mixer.music.play(loop)

    @staticmethod
    def stop():
        """
        Stops playing the music
        """
        pygame.mixer.music.stop()
