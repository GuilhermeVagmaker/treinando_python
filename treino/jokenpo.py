import random

def jogar_jokenpo():
  jogo = ["pedra", "papel", "tesoura"]

  print("==========================================================")
  print("========================JOKENPO===========================")
  print("==========================================================\n")

  def jokenpo(player_1, player_2, jg_escolha):

    if player_1 == "":
        player_1 = "CPU 1"

    if player_2 == "":
        player_2 = "CPU 2"

    if player_1 != "CPU 1":
        jogada_player1 = jg_escolha
    else:
        jogada_player1 = random.choice(jogo)

    if player_2 == "CPU 2":
        jogada_player2 = random.choice(jogo)
      
    if jogada_player1 == "tesoura" and jogada_player2 == "papel":
      print(f"\n{player_1} jogou {jogada_player1} e {player_2} jogou {jogada_player2}")
      print(f"\n{player_1} Venceu, Parabéns!!!")
      print(input("\nAperte ENTER para continuar..."))

    elif jogada_player1 == "pedra" and jogada_player2 == "tesoura":
      print(f"\n{player_1} jogou {jogada_player1} e {player_2} jogou {jogada_player2}")
      print(f"\n{player_1} Venceu, Parabéns!!!")
      print(input("\nAperte ENTER para continuar..."))
      
    elif jogada_player1 == "papel" and jogada_player2 == "pedra":
      print(f"\n{player_1} jogou {jogada_player1} e {player_2} jogou {jogada_player2}")
      print(f"\n{player_1} Venceu, Parabéns!!!")
      print(input("\nAperte ENTER para continuar..."))

    elif jogada_player1 == jogada_player2 :
      print(f"\n{player_1} jogou {jogada_player1} e {player_2} jogou {jogada_player2}")
      print("\nDeu empate")
      print(input("\nAperte ENTER para continuar..."))

    else:
      print(f"\n{player_2} jogou {jogada_player2} e {player_1} jogou {jogada_player1}")
      print(f"\n{player_2} Venceu, Parabéns!!!")
      print(input("\nAperte ENTER para continuar..."))

  nome_usuario = input("\nEscolha um nome para o jogador: ")

  while True:
  
    print("\n(1) - oJogar")
    print("(2) - Sair\n")

    try:
        escolha_menu = int(input("Oque deseja no momento? "))
    except ValueError:
      print("\nApenas números são validos\n")
      continue
    if escolha_menu <= 0 or escolha_menu > 2:
      print("\nDigite apenas números entre 1 e 2\n")
      continue

    if escolha_menu == 1:

      while True:
    
        print("\n(1) - J1 vs CPU")
        print("(2) - CPU vs CPU\n")

      
        try:
          player = int(input("Escolhe como deseja jogar: "))
        except ValueError:
          print("\nApenas números são validos")
          continue
        if player <= 0 or player > 2:
          print("\nDigite apenas números entre 1 e 2")
          continue
        
        if player == 1:
          print("\nApenas o player 1 ira jogar")

          while True: 
            
            print("\n(1) - Pedra")
            print("(2) - Papel")
            print("(3) - Tesoura\n")

            try:
              escolha_player = int(input("Escolha uma das opções acima pra jogar: "))
            except ValueError:
              print("\nApenas números são validos")
              continue
            if escolha_player <= 0 or escolha_player > 3:
              print("\nDigite apenas números entre 1 e 3")
              continue
            

            
            if escolha_player == 1:
              escolha_player = "pedra"
              break
            elif escolha_player == 2:
              escolha_player = "papel"
              break
            elif escolha_player == 3:
              escolha_player = "tesoura"
              break
            else: 
              print("não existe essa escolha")

          jokenpo(nome_usuario,"", escolha_player)
          break
        elif player == 2:
          print("\nOs bots vão jogar agora")
          jokenpo("","","")
          break
    elif escolha_menu == 2:
      print("\nEncerrando jokenpo...")
      break
