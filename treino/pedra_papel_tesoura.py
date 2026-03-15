import random
jogo = ["pedra", "papel", "tesoura"]



def jokenpo(player_1, player_2, jg_escolha):

  rand = random.choice(jogo) 
  true_jogada = ""

  if player_1 == "":
    player_1 = "CPU 1"
  elif player_2 == "":
    player_2 = "CPU 2"
  elif player_1 and player_2 == "":
    player_2 = "CPU"

  if player_1 and jg_escolha:
    true_jogada  = jg_escolha
  elif player_1 == "CPU 1" and jg_escolha == "":
      true_jogada = rand
  else:
    print("jogador não escolheu uma das opçãos, o CPU jogar  none = a pelo jogador")
    true_jogada = rand
    
  if player_1 == "tesoura" and player_2 == "papel":
    print(f"{player_1} jogou {true_jogada} e {player_2} jogou {rand}")
    print(f"{player_1} Venceu, Parabéns!!!")

  elif player_1 == "pedra" and player_2 == "tesoura":
    print(f"{player_1} jogou {true_jogada} e {player_2} jogou {rand}")
    print(f"{player_1} Venceu, Parabéns!!!")
    
  elif player_1 == "papel" and player_2 == "pedra":
    print(f"{player_1} jogou {true_jogada} e {player_2} jogou {rand}")
    print(f"{player_1} Venceu, Parabéns!!!")

  elif player_1 == player_2:
    print(f"{player_1} jogou {true_jogada} e {player_2} jogou {rand}")
    print("Deu empate")

  else:
    print(f"{player_2} jogou {true_jogada} e {player_1} jogou {rand}")
    print(f"{player_2} Venceu, Parabéns!!!")
  



while True:
  def menu():
    print("(1) - Jogar")
    print("(2) - Sair")
  menu()

  escolha_menu = int(input("Oque deseja no momento? "))

  if escolha_menu == 1:

    while True:
    
      print("(1) - J1 vs J2")
      print("(2) - J1 vs CPU")
      print("(3) - CPU vs CPU")

      player = int(input("Escolhe como deseja jogar: "))
      
      if player == 1:

        print("Função ainda em andamento")
        continue

        print("Os dois player vão jogar")
        player_1 = input("Digite um nome para o player 1: ")
        player_2 = input("Digite um nome para o player 2: ")

        jokenpo(player_1, player_2)
        break
      elif player == 2:
        print("Apenas o player 1 ira jogar")
        nome_usuario = input("Escolha um nome para o jogador 1: ")

        while True: 
          
          print("(1) - Pedra")
          print("(2) - Papel")
          print("(3) - Tesoura")

          escolha_player = int(input("Escolha uma das opções acima pra jogar: "))

          
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
      elif player == 3:
        print("Os bots jogaram agora")
        jokenpo("","","")
        break
      else:
        print("Valor não encontrado nas opção, coloca uma opção valída")
  elif escolha_menu == 2:
    print("Encerrando jokenpo...")
    break
