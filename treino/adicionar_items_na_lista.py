lista = []

while True:

    print("\n(1) - Colocar um item a lista")
    print("(2) - Ver lista")
    print("(3) - sair \n")

    escolha_usuario = int(input("Escolha uma das opções acima: "))

    if escolha_usuario ==  1:
        item_a_ser_adicionado = input("\nQual item deseja lista? ")
        lista.append(item_a_ser_adicionado)
        print("\nItem adicionado com sucesso !!!\n")
    elif escolha_usuario == 2: 

        if len(lista) == 0:
            print("Nenhum item adicionado ate o momento")
            
        print("Os items Adicionado até o momento são: \n")
        for item in lista:
            print(item)
    elif escolha_usuario == 3:
        print("Encerando...\n")
        break
    else:
        print("Nenhuma opção encontrada\n")
    
