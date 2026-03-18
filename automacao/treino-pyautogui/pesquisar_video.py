import pyautogui
import time

pyautogui.FAILSAFE = True
def tab_youtube(quantidade_tabs):
  for i in range(int(quantidade_tabs)):
    time.sleep(0.5)
    pyautogui.press("tab")

def pesquisar_youtube(pesquisa):
  pyautogui.write(pesquisa, interval=0.05)
  time.sleep(1)
  pyautogui.press("enter")
  time.sleep(1)
  pyautogui.moveTo(x=721, y=512)
  time.sleep(1)
  pyautogui.click(button="middle")
  time.sleep(1)

# time.sleep(3)
# print(pyautogui.position())

time.sleep(3)
pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("Brave")
time.sleep(1)   
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("ctrl","l")
time.sleep(1)
pyautogui.write("youtube.com")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)
tab_youtube(4)
time.sleep(3)
pesquisar_youtube("python automacao")
time.sleep(1)
pyautogui.moveTo(x=741, y=194)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.hotkey("ctrl","shift","backspace")
time.sleep(1)
pesquisar_youtube("pyautogui tutorial")
time.sleep(1)
pyautogui.moveTo(x=741, y=194)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.hotkey("ctrl","shift","backspace")
time.sleep(1)
pesquisar_youtube("python bots")

for i in range(3):
  time.sleep(1)
  pyautogui.hotkey("ctrl","tab")

