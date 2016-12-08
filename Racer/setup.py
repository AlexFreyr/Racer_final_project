# coding=utf-8
"""
Game executable file
"""

import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("distribution.py", base=base)]

cx_Freeze.setup(
    name="Racer",
    options={"build_exe": {"packages":["tkinter", "pygame", "pymysql", "bcrypt"], "include_files": ["src/blue_car.png", "src/cars.png", "src/mainroad.png"]}},
    version="0.01",
    description="Racer game",
    executables=executables
)
