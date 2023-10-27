import pyautogui
import keyboard

running = True
while running == True:
    pyautogui.press('capslock', interval=0.15)
    if keyboard.is_pressed('q') and keyboard.is_pressed('w') and keyboard.is_pressed('o') and keyboard.is_pressed('p'):
        running = False
