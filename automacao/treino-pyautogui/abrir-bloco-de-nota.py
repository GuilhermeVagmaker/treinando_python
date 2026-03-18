import pyautogui
import time

pyautogui.FAILSAFE = True


time.sleep(3)
pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("editor de texto", interval=0.1)
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("Aprendendo a usar o pyautogui!", interval=0.1)
