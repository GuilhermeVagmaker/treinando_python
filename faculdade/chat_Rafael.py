import random

lista_frase_motivacional = [
      "\nGrandes resultados começam com pequenos passos dados todos os dias",
      "\nA disciplina te leva a lugares onde a motivação sozinha nunca chega",
      "\nTodo especialista já foi um iniciante que não desistiu.",
      "\nSe hoje foi difícil, é porque você está evoluindo.",
      "\nO esforço de hoje é a conquista de amanhã.",
      "\nQuem insiste um pouco mais acaba chegando mais longe.",
      "\nCada erro é apenas mais um passo em direção ao acerto.",
      "\nVocê não precisa ser perfeito, apenas constante.",
      "\nA diferença entre quem consegue e quem desiste é a persistência.",
      "\nPequenos progressos diários constroem grandes conquistas.",
      "\nO sucesso é construído na rotina, não na sorte.",
      "\nContinue mesmo quando estiver cansado — a vitória, pode estar logo depois.",
      "\nNão compare seu começo com o meio do caminho de outra pessoa.",
      "\nA dedicação transforma sonhos em realidade.",
      "\nQuanto mais você pratica, mais a sorte parece aparecer.",
      "\nSeu futuro agradece o esforço que você faz hoje.",
      "\nAprender algo novo todos os dias é um investimento em si mesmo.",
      "\nA persistência vence o talento quando o talento desiste.",
      "\nA jornada pode ser longa, mas cada passo vale a pena.",
      "\nVocê é capaz de muito mais do que imagina."
      ]
lista_curiosidades_aleatorias = [
      "Polvos têm três corações.",
      "O mel nunca estraga — já foram encontrados potes de mel com mais de 3 mil anos ainda comestíveis.",
      "Bananas são radioativas, mas em um nível extremamente pequeno e seguro.",
      "O coração de uma baleia azul pode pesar mais de 180 kg.",
      "Existem mais árvores na Terra do que estrelas na Via Láctea (estimativa científica).",
      "O polvo possui sangue azul.",
      "A Lua está se afastando da Terra cerca de 3,8 cm por ano.",
      "Tubarões existem há mais tempo que as árvores.",
      "As lontras dormem de mãos dadas para não se separarem enquanto flutuam.",
      "Um dia em Vênus é mais longo que um ano em Vênus.",
      "O cérebro humano tem cerca de 86 bilhões de neurônios.",
      "As girafas têm o mesmo número de vértebras no pescoço que os humanos (7)",
      "O cheiro da chuva no chão seco tem um nome: petricor.",
      "Algumas tartarugas podem respirar pelo traseiro durante a hibernação.",
      "O DNA humano é aproximadamente 60% igual ao de uma banana.",
      "Existe um tipo de água-viva que é biologicamente imortal.",
      "Um raio é cinco vezes mais quente que a superfície do Sol.",
      "O maior organismo vivo do planeta é um fungo gigante nos EUA que ocupa quilômetros de floresta.",
      "As formigas não têm pulmões — elas respiram por pequenos buracos no corpo.",
      "O Tiranossauro Rex viveu mais perto da época atual do que da época do Estegossauro."
    ]

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
  print("(5) 🚪 Sair\n")

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

        elif msg == "tudo bem":
            print("Alpha: Estou funcionando perfeitamente! 😄")

        elif msg == "qual seu nome":
            print("\nAlpha: Eu o Alpha um chatbot simples criado em Python.")

        elif msg == "quem te criou":
            print("\nAlpha: Meu criador se chama Guilherme")

        else:
           print("Alpha: Hmm... não entendi 🤔")
           print("Frases que conheço: 'oi', 'ola', 'tudo bem', 'qual seu nome', 'quem te criou'\n")
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
    
  elif escolha_usuario == 5:
    print("Encerrando Alpha chat bot...")
    print(f"Até mais {nome_usuario}, espero te ver novamente")
    print("Chat encerrado.")
    break
  else:
     print(f"O numero {escolha_usuario} não está nas opção mencionadas acima, escolha um número entre as opção do menu para usar o bot corretamente")