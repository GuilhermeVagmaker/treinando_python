senhas = []
senha_verdadeira = input("Digite uma senha: ")
senhas.append(senha_verdadeira)
while True: 
  usuario = input("Digite a senha novamente: ")
  if usuario in senhas:
    print("Senha correta!!")
    break
  else:
    print("Senha incorreta!!")
