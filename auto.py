personagem = []

classes = [
    "Bárbaro", "Bardo", "Bruxo", "Clérigo", "Druida", "Feiticeiro", "Guerreiro", "Ladino", "Mago", "Monge", "Paladino", "Patrulheiro", "Artífice"
]

racas = [
    "Humano", "Anão", "Elfo", "Halfling", "Gnomo", "Tiefling", "Draconato", "Meio-Elfo", "Meio-Orc", "Orc", "Goblin", "Kobold", "Tabaxi", "Aarakocra", "Goliath", "Firbolg", "Tritão", "Genasi", "Warforged"
]


def guarda_personagens():
  
  nome_jogador = input("Nome do jogador: ")
  nome_personagem = input("Nome do personagem: ")
  tipo = input("Classe ou Subclasse? ")
  
  classe_sub = None
  classe_escolhida = None
  
  if tipo.lower() == "classe":
    for i, classe in enumerate(classes, start=1):
     print(f"{i}: {classe}")
    escolha_classe = input("Escolha uma classe: ")
    if escolha_classe.isdigit():
      classe_escolhida = int(escolha_classe) - 1
      if 0 <= classe_escolhida < len(classes):
        classe_escolhida = classes[classe_escolhida]
        classe_sub = "Classe"
      else:
        print("A classe selecionadas não existe")
        return
    else:
        print("Apenas numero são valido nessa escolha")
        return
    
    
    
  elif tipo.lower() == "subclasse":
    for i, classe in enumerate(classes, start=1):
      print(f"{i}: {classe}")
    subclasse_1 = input(f"Escolha a primera classe:  ")
    subclasse_2 = input(f"Escolha a segunda classe:  ")
    if not subclasse_1.isdigit() or not subclasse_2.isdigit():
      indice_1 = int(subclasse_1) - 1  
      indice_2 = int(subclasse_2) - 1 
    if 0 <= indice_1 < len(classes) and 0 <= indice_2 < len(classes):
      classe_escolhida = [
        classes[indice_1],
        classes[indice_2]
      ]
      classe_sub = "Subclasse"
    else:
      print("Uma das subclasses selecionadas não existe")
      return
  else:
    print("Essa opção não é valida")
    return
  
  
    
  print("Selecione uma raça: ")
  for i, raca in enumerate(racas, start=1):
    print(f"{i}: {raca}")
  
  selecionando_raca = input("Selecione uma raça: ")
  if selecionando_raca.isdigit():
    raca_escolhida = int(selecionando_raca) - 1
    if 0 <= raca_escolhida < len(classes):
      raca_escolhida = classes[raca_escolhida]
    else:
      print("A Raça selecionadas não existe")
      return
  else:
      print("Apenas numero são valido nessa escolha")
      return

  
  personagem.append({
    "nome_jogador": nome_jogador,
    "nome_personagem": nome_personagem,
    classe_sub: classe_escolhida,
    "raça": raca_escolhida
  })
  
guarda_personagens()
print(personagem)