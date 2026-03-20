import pyautogui
import time


# time.sleep(5)
# print(pyautogui.position())

pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("Brave")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("ctrl","l")
time.sleep(1)
pyautogui.write("https://web.whatsapp.com/", interval=0.02)
time.sleep(1)
pyautogui.press("enter")
time.sleep(4)
while True:
    try:
        imagem = pyautogui.locateOnScreen("whatsapp.png", confidence=0.7)

        if imagem:
            print("whatsapp carregando")
            time.sleep(1)
        else:
            break

    except:
        print("whatsapp carregou")
        break
    
time.sleep(5)

posicao_barra_pesquisa = pyautogui.locateCenterOnScreen("barra_pesquisa.png", confidence=0.5)
if posicao_barra_pesquisa:
  pyautogui.click(posicao_barra_pesquisa)
  time.sleep(1)

  pyautogui.write("Buzao sama", interval=0.02)

time.sleep(2)

posicao_teste_bot = pyautogui.locateCenterOnScreen("grupo_onibus.png", confidence=0.6)
if posicao_teste_bot:
  pyautogui.click(posicao_teste_bot)
  time.sleep(2)

 


while True:
    try:
        posicao_univc = pyautogui.locateCenterOnScreen("univc.png", confidence=0.5)
        posicao_univc2 = pyautogui.locateCenterOnScreen("univc_minusculo.png", confidence=0.5)

        if posicao_univc or posicao_univc2:
              print("Enquete encontrada")
              pyautogui.click(posicao_univc)
              print("Tarefa conclúida")
              print("Encerrando...")
              break
        else:
            break

    except:
        print("Não achou ainda a enquete, Aguarde...")
        time.sleep(60)
        continue

