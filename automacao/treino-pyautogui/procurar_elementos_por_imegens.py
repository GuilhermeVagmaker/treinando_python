import pyautogui
import time

pyautogui.FAILSAFE = True

time.sleep(3)
pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("brave")
time.sleep(1)
pyautogui.press("enter")

time.sleep(3)
pyautogui.hotkey("ctrl","l")
time.sleep(1)
pyautogui.write("youtube.com")
time.sleep(1)
pyautogui.press("enter")

time.sleep(5)

posicao = pyautogui.locateCenterOnScreen("search.png", confidence=0.8)

if posicao:
    pyautogui.click(posicao)
    time.sleep(1)

    pyautogui.write("python automacao", interval=0.05)
    pyautogui.press("enter")

else:
    print("imagem nao encontrada")