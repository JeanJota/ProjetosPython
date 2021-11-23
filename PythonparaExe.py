import sys
from cx_Freeze import setup, Executable

from selenium import webdriver
import time

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

base = None
icon = "icon.ico"


if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "interface",
        version = "2.0",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("BotNavegador.py", base=base, icon=icon)])