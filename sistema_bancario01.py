import datetime as dt

MENU = """ 

[d] Depositar
[s] Sacar
[e] Extrato 
[q] Sair

"""

saldo = 10000
extrato = []
contador = 0
LIMITE_DIARIO_TRANSACAO = 10

def executa_deposito():
    global saldo, extrato, contador
    print("Depósito")
    deposito = float(input("Qual valor deseja depositar? "))

    if deposito > 0:
        print(f"Depositado R$ {deposito:.2f}")
        saldo += deposito
        extrato.append(deposito)
    else:
        print("Impossivel realizar seu depósito!")

def executa_saque():
    global saldo, extrato, contador
    print("Sacar")
    saque = float(input("Qual valor deseja sacar? "))
        
    if contador > LIMITE_DIARIO_TRANSACAO:
        print("Excedeu o limite de transações diárias")

    elif saldo > saque:
        print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
        contador += 1
        saldo -= saque

        data = dt.datetime.now()
        data_hora_pt_br = data.strftime("%d/%m/%Y %H:%M:%S") 
        nova_transacao = [contador, -(saque), data_hora_pt_br]
        extrato.append(nova_transacao)

    else:
        print("Saldo insuficiente!")

def executa_extrato():
    print("Extrato")
    if extrato == []:
        print("Não foram realizadas movimentações.")

    for transacao in extrato:
        print(f"R$ {transacao[1]:10.2f} : {transacao[2]}")
    print(f"Seu saldo atual é de R$ {saldo:.2f}")

def main():
    print ("Olá, seja bem vindo ao LeleBank")
    global saldo
    while True: 
        print("=" * 50)
        print(MENU)
        opcao = input("Informe qual opção você deseja:")    
        
        if opcao.lower() == "d":
            executa_deposito()            

        elif opcao.lower() == "s":
            executa_saque()                

        elif opcao.lower () == "e":
            executa_extrato()

        elif opcao.lower() == "q":
            print("\33[2;33;44mObrigada por ser cliente LeleBank, tenha um bom dia!\33[m")
            break

        else:
            print("Opcão inválida, tente novamente!")

main()

