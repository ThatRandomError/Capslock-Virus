import pyautogui, keyboard

while True:
    pyautogui.press('capslock', interval=0.15)
    if keyboard.is_pressed('q') and keyboard.is_pressed('w') and keyboard.is_pressed('o') and keyboard.is_pressed('p'):
        break
