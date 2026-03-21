import pyautogui
import time
import os

if not os.path.exists("prints"):
  os.mkdir("prints")

print("bot de monitoramento...")
print(" o bot vai começar em 5 segundos...")

time.sleep(5)

print_atual = pyautogui.screenshot()

contador = 1

while True:

  print_nova = pyautogui.screenshot()
  time.sleep(2)

  if print_nova != print_atual:
    print(f"Novas mudancas Detectadas:")
    nome = f"prints/mudanca_{contador}.png"
    print_nova.save(nome)
    print(f"Screenshot salva: {nome}")
    contador += 1
    print_atual = print_nova
  