class ContaBancaria:
  def __init__(self,saldo ):
    self.__saldo = saldo

  
  def verSaldo(self):
    print(f"\nseu saldo atualmente é de R$: {self.__saldo}\n")
    if self.__saldo == "":
      self.__saldo = 0


  def depositarSaldo(self):
    if self.__saldo == 100000:
      print("\nA sua conta barcaria ja chegou no saldo limite\n")
    else:
      depositar = int(input("\nQuanto que deseja depositar: "))
      if depositar > 100000 or (depositar + self.__saldo > 100000):
          print("O deposito passa o limite de 100.000 do banco, não sera possivel realizar o deposito")
      else:
          self.__saldo += depositar
          print(f"\nO deposito foi um sucesso, atualmente seu saldo é de {self.__saldo}\n")
        
  
  def retirarSaldo(self):

    if self.__saldo == 0:
      print("\nAtualmente a sua conta não tem saldo, deposite mais saldo para conseguir retirar")
    else:
      print(f"\nO saldo atual da sua conta é de: R${self.__saldo}")
      saque = int(input("\nQual o valor que deseja retirar: "))

      if  saque > self.__saldo:
        print(f"\nA conta atualmente tem {self.__saldo}, não tem como fazer o saque desejado\n")
      else:
        self.__saldo -= saque
        print(f"\nO saque foi um sucesso, atualmente seu saldo é de {self.__saldo}\n")

  def bancoOn(self):

    print("\n===============================================")
    print("=============Bem vindo ao banco Nox============")
    print("===============================================\n")

    while True:      

      input("\nPress enter for continue...")
      print("\nEscolha um dos serviços do banco: ")
      print("\n(1) - Ver saldo")
      print("(2) - Depositar saldo")
      print("(3) - Sacar saldo")
      print("(4) - Sair do banco\n")

      try:
        escolha_user = int(input(":"))
      except ValueError:
        print("Apenas números são permitidos")
        continue

      if escolha_user == 1:
        self.verSaldo()

      elif escolha_user == 2:
        self.depositarSaldo()

      elif escolha_user == 3:
        self.retirarSaldo()

      elif escolha_user == 4:
        print("Encerrando banco nox...")
        print("Adeus Usuario, espero telo aqui novamente!!")
        break

      else:
        print("Opção não encontrada, escolha umas das opção mencionadas no menu.")

  # def retirarSaldo(self):

conta = ContaBancaria(0)
conta.bancoOn()