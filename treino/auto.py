personagens = []

classes = [
    "Bárbaro", "Bardo", "Bruxo", "Clérigo", "Druida", "Feiticeiro",
    "Guerreiro", "Ladino", "Mago", "Monge", "Paladino",
    "Patrulheiro", "Artífice"
]

racas = [
    "Humano", "Anão", "Elfo", "Halfling", "Gnomo", "Tiefling",
    "Draconato", "Meio-Elfo", "Meio-Orc", "Orc", "Goblin",
    "Kobold", "Tabaxi", "Aarakocra", "Goliath", "Firbolg",
    "Tritão", "Genasi", "Warforged"
]


def guarda_personagens():

    nome_jogador = input("\nNome do jogador: ")
    nome_personagem = input("Nome do personagem: ")
    tipo = input("Classe ou Subclasse? ").lower()

    classe_sub = None
    classe_escolhida = None

    # ===== ESCOLHA DE CLASSE =====
    if tipo == "classe":
        print("\nEscolha uma classe:")
        for i, classe in enumerate(classes, start=1):
            print(f"{i}: {classe}")

        escolha_classe = input("Número da classe: ")

        if not escolha_classe.isdigit():
            print("Apenas números são válidos")
            return

        indice = int(escolha_classe) - 1

        if 0 <= indice < len(classes):
            classe_escolhida = classes[indice]
            classe_sub = "Classe"
        else:
            print("Classe inválida")
            return

    # ===== ESCOLHA DE SUBCLASSE =====
    elif tipo == "subclasse":
        print("\nEscolha duas classes:")
        for i, classe in enumerate(classes, start=1):
            print(f"{i}: {classe}")

        sub1 = input("Primeira classe: ")
        sub2 = input("Segunda classe: ")

        if not sub1.isdigit() or not sub2.isdigit():
            print("Apenas números são válidos")
            return

        indice_1 = int(sub1) - 1
        indice_2 = int(sub2) - 1

        if 0 <= indice_1 < len(classes) and 0 <= indice_2 < len(classes):
            classe_escolhida = [
                classes[indice_1],
                classes[indice_2]
            ]
            classe_sub = "Subclasse"
        else:
            print("Uma das subclasses não existe")
            return

    else:
        print("Opção inválida (use 'classe' ou 'subclasse')")
        return

    # ===== ESCOLHA DE RAÇA =====
    print("\nEscolha uma raça:")
    for i, raca in enumerate(racas, start=1):
        print(f"{i}: {raca}")

    escolha_raca = input("Número da raça: ")

    if not escolha_raca.isdigit():
        print("Apenas números são válidos")
        return

    indice_raca = int(escolha_raca) - 1

    if 0 <= indice_raca < len(racas):
        raca_escolhida = racas[indice_raca]
    else:
        print("Raça inválida")
        return
    
    id_personagem = len(personagens) + 1

      


    # ===== SALVAR PERSONAGEM =====
    personagens.append({
        "id": id_personagem,
        "nome_jogador": nome_jogador,
        "nome_personagem": nome_personagem,
        classe_sub: classe_escolhida,
        "raça": raca_escolhida
    })

    print("\n✅ Personagem criado com sucesso!")

def listar_personagens():
  print("\n📜 PERSONAGENS CADASTRADOS: \n")
  for personagem in personagens:
    print(f"{personagem}\n")
# ===== EXECUÇÃO =====

while True:
  print("\n1 - Criar personagem")
  print("2 - Mostrar personagens criados")
  print("3 - Encerrar programa")
  
  
  opcao = input("\nOq deseja fazer? ")
  
  if not opcao.isdigit():
    print("Apenas números são validos")
    break
  
  numero_validado  = int(opcao)
  
  if numero_validado == 1:
    guarda_personagens()
  if numero_validado == 2:
    listar_personagens()
  if numero_validado == 3:
    print("Encerrando programa....")
    break
    
    
    
    