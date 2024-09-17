print ("Olá, seja bem vindo ao LeleBank")

#aula de string_4 
MENU = """ 

[d] Depositar
[s] Sacar
[e] Extrato 
[q] Sair

"""

saldo = 0.0
limite = 500
extrato = []

#aula de estrutura de repetição e break
while True: 
    print(MENU)
    opcao = input("Informe qual opção você deseja:")
    
    
    if opcao.lower() == "d":
        print("Depósito")
        deposito = float(input("Qual valor deseja depositar?"))
        saldo += deposito 

    elif opcao.lower() == "s":
        print("Sacar")
        saque = float(input("Qual valor deseja sacar?"))
        saldo -= saque

    elif opcao.lower () == "e":
        print(f"Extrato {saldo}")

    elif opcao.lower() == "q":
        break

    else:
        print("Opcão inválida, tente novamente!")

