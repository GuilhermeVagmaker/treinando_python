import random

def jogar_adivinha():
  rand_number = random.randint(1,100)
  contador = 0

  print("\n============================================================")
  print("====================Adivinhe o número=======================")
  print("============================================================\n")

  while True:

    try:
      usuario = int(input("\nDigite um número entre 1 e 100: "))
    except ValueError:
        print("Apenas números são validos")
        continue
    
    if usuario <= 0 or usuario > 100:
      print("\nDigite apenas números entre 1 e 100")
      continue
    
    contador += 1

    if usuario == rand_number:
      print("\nParabéns, você acertou o número \n")
      print(f"Foram {contador} tentativas até acertar")
      break
    elif usuario > rand_number:
      print("\nO número está acima do número certo")
    else:
      print("\nO número está abaixo do número certo")
