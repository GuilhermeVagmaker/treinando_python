import pyautogui
import time


print("O bot começara em 5 segundos")
time.sleep(5)

for i in range(1,5):
  screenshot = pyautogui.screenshot()
  screenshot.save(f"foto_{i}.png")
  print(f"screenshot salva: foto_{i}.png")
  time.sleep(3)