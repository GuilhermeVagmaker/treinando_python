print("\nOlá, tudo bem?")
print("Qual seu nome ? \n")

while True:
    nome = input("Insira seu nome: ")

    if not nome.isalpha():
        print(" Você está usando numeros a invez de letras, insira seu nome corretamente\n")
    
    elif len(nome) > 75:
        print(f"Seu nome não tem essa quantidade de letras digite novamente\n")
    
    else:
        print(f"\nPrazer, {nome}, é um prazer ter você aqui\n")
        break


print("Quantos anos vc tem ? \n")

while True:
    idade =  input("Insira a sua idade: ")

    if not idade.isdigit(): 
        print("\nVocê está usando letras a invez de numeros, insira sua idade corretamente\n")
    
    elif int(idade)>= 100 or int(idade) <= 17:
        print(f"\nVocê não tem {idade} anos\n")

    else:
        print(f"\nSeu nome é {nome}, e atualmente você tem {idade} anos \n")
        break