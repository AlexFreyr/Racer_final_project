# coding=utf-8
"""
Game executable file
"""

from distutils.core import setup
import py2exe

setup(name="Racer",
      version="1.0",
      description="Racer game",
      data_files=[("", ["src/mainroad.png", "src/cars.png", "src/blue_car.png", "Music/racer.mp3"])],
      console=["distribution.py"])
