print ("Olá, seja bem vindo ao LeleBank")

MENU = """ 

[d] Depositar
[s] Sacar
[e] Extrato 
[q] Sair

"""

saldo = 0.0
extrato = []
LIMITE_SAQUE = 3
LIMITE_DIARIO = 500

while True: 
    print("=" * 50)
    print(MENU)
    opcao = input("Informe qual opção você deseja:")    
    
    if opcao.lower() == "d":
        print("Depósito")
        deposito = float(input("Qual valor deseja depositar? "))

        if deposito > 0:
            print(f"Depositado R$ {deposito:.2f}")
            saldo += deposito
            extrato.append(deposito)
        else:
            print("Impossivel realizar seu depósito!")

    elif opcao.lower() == "s":
        print("Sacar")
        saque = float(input("Qual valor deseja sacar? "))
        
        contador = 0
        for transacao in extrato:
            if transacao < 0:
                contador += 1

        if contador >= LIMITE_SAQUE:
            print("Excedeu o limite de saques diários")
            
        elif saque > LIMITE_DIARIO:
            print(f"Saque de R$ {saque:.2f} excede o limite diário de R$ {LIMITE_DIARIO:.2f}")

        elif saldo > saque:
            print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
            saldo -= saque
            extrato.append(-(saque))
        else:
            print("Saldo insuficiente!")
            

    elif opcao.lower () == "e":
        print("Extrato")
        if extrato == []:
            print("Não foram realizadas movimentações.")

        for transacao in extrato:
            print(f"R$ {transacao:.2f}")
        print(f"Seu saldo atual é de R$ {saldo:.2f}")

    elif opcao.lower() == "q":
        print("\33[2;33;44mObrigada por ser cliente LeleBank, tenha um bom dia!\33[m")
        break

    else:
        print("Opcão inválida, tente novamente!")

