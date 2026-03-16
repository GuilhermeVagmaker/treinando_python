from jogos.adivinhe_o_numero import jogar_adivinha
from jogos.jokenpo import jogar_jokenpo

from listas.lista_mot import lista_curiosidades_aleatorias
from listas.lista_mot import lista_frase_motivacional
import random

print("=================================================")
print("================  ALPHA CHAT BOT ================")
print("=================================================\n\n")

nome_usuario = input("Insira o seu nome: ")

if not nome_usuario.isalpha():
   print("Apenas letras são permitido, insira seu nome corretamente")

print(f"\nPrazer em te conhecer {nome_usuario}")
print(f"Eu sou o Alpha, um chat bot, aonde vou ter algumas pequenas interrações com você {nome_usuario}\n")

while True: 

  input("\nAperte ENTER para continuar...")

  print("\nO que você gostaria de fazer?\n") 

  print("\n==================== 📋 MENU ======================\n")
  print("(1) 💬 Conversar")
  print("(2) 🌟 Ver uma frase motivacional")
  print("(3) 🧠 Saber uma curiosidade")
  print("(4) 🎯 Adivinhe o número")
  print("(5) 🎮 Jokenpo")
  print("(6) 🚪 Sair\n")

  try:
    escolha_usuario = int(input(":"))
  except ValueError:
     print("\nApenas números são validos\n") 
     continue
  
  if escolha_usuario == 1:
    print("\nChat iniciado! (digite 'sair' para voltar ao menu)\n")

    while True:
        msg = input("Você: ").lower()

        if msg == "sair":
            print("Bot: Voltando ao menu...")
            break

        elif msg == "oi" or msg == "ola":
            print("Alpha: Olá! Como você está? 😊")

        elif msg == "tudo bem?":
            print("Alpha: Estou funcionando perfeitamente! 😄")

        elif msg == "qual seu nome?":
            print("\nAlpha: Eu o Alpha um chatbot simples criado em Python.")

        elif msg == "quem te criou?":
            print("\nAlpha: Meu criador se chama Guilherme")

        else:
           print("Alpha: Hmm... não entendi 🤔")
           print("Frases que conheço: 'oi', 'ola', 'tudo bem?', 'qual seu nome?', 'quem te criou?'\n")
  elif escolha_usuario == 2:

    if lista_frase_motivacional:
      frase_aleatoria = random.choice(lista_frase_motivacional)
      print(frase_aleatoria)
      lista_frase_motivacional.remove(frase_aleatoria)
    else:
      print("\nAs frases motivacionais acabaram, mas o mais importante é você saber que você é alguém incrível, e eu espero que você nunca desista")


  elif escolha_usuario == 3:

    if lista_curiosidades_aleatorias:
      frase_aleatoria = random.choice(lista_curiosidades_aleatorias)
      print(frase_aleatoria)
      lista_curiosidades_aleatorias.remove(frase_aleatoria)
    else:
      print("As curiosidades acabaram, mas nunca pare de querer adquirir conhecimento, sempre corra atrás de saber saber mais, conhecimento nunca é demais")

  elif escolha_usuario == 4:
    jogar_adivinha()
  elif escolha_usuario == 5:  
    jogar_jokenpo()
  elif escolha_usuario == 6:
    print("\nEncerrando Alpha chat bot...")
    print(f"Até mais {nome_usuario}, espero te ver novamente! 😊\n")
    print("Chat encerrado.")
    break
  else:
     print(f"\nO numero {escolha_usuario} não está nas opção mencionadas acima, escolha um número entre as opção do menu para usar o bot corretamente")