print ("Olá, seja bem vindo ao LeleBank")

#aula de string_4 
MENU = """ 

[d] Depositar
[s] Sacar
[e] Extrato 
[q] Sair

"""
#aula de estrutura de repetição e break
while True: 
    print (MENU)
    opcao = input("Informe qual opção você deseja:")
    


    if opcao == "d":
        print("Depósito")

    elif opcao == "s":
        print("Sacar")

    elif opcao == "e":
        print("Extrato")

    elif opcao == "q":
        break

