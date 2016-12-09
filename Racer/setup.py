# coding=utf-8
"""
Game executable file
"""

from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [Executable("main.py", base=base)]
packages = ["tkinter", "pygame", "pymysql", "bcrypt"]
files = ["src/blue_car.png", "src/cars.png", "src/mainroad.png", "Music/racer.mp3",
         "Background", "Buttons", "Car", "Login", "Menu", "Music", "Score", "Settings",
         "Start", "Text", "README"]

setup(
    name="Racer",
    options={"build_exe": {"packages": packages, "include_files": files}},
    version="0.01",
    description="Racer game",
    executables=executables
)
