import datetime as dt

def executa_deposito(extrato, contador, limite_diario_transacao, /) -> float | int:
    novo_saldo = 0
    novo_contador = 0
    print("Depósito")
    deposito = float(input("Qual valor deseja depositar? "))

    if contador > limite_diario_transacao:
        print("Excedeu o limite de transações diárias")

    elif deposito > 0:
        print(f"Depósito:\t\tR$ {deposito:.2f}")
        print("===Depósito realizado com sucesso!===")
        novo_contador += 1
        novo_saldo += deposito

        data = dt.datetime.now()
        data_hora_pt_br = data.strftime("%d/%m/%Y %H:%M:%S") 
        nova_transacao = [contador, deposito, data_hora_pt_br]
        extrato.append(nova_transacao)

    else:
        print("Impossivel realizar seu depósito!")

    return novo_saldo, novo_contador

def executa_saque(*,saldo, extrato, contador, limite_diario_transacao) -> float | int:
    novo_saldo = 0
    novo_contador = 0
    print("Sacar")
    saque = float(input("Qual valor deseja sacar? "))
        
    if contador > limite_diario_transacao:
        print("Excedeu o limite de transações diárias")

    elif saque > saldo:
        print("Saldo insuficiente!")

    elif saque > 0:
        novo_saldo -= saque
        extrato += f"Saque:\t\tR$ {saque:.2f}"
        novo_contador += 1
        print("===Saque realizado com sucesso!===")

        data = dt.datetime.now()
        data_hora_pt_br = data.strftime("%d/%m/%Y %H:%M:%S") 
        nova_transacao = [contador, -(saque), data_hora_pt_br]
        extrato.append(nova_transacao)

    else:
        print("Saque inválido!")

    return novo_saldo, novo_contador

def executa_extrato(saldo, / , * , extrato):
    print("Extrato")
    if extrato == []:
        print("Não foram realizadas movimentações.")

    for transacao in extrato:
        if isinstance(transacao, list):
            print(f"R$ {transacao[1]:10.2f} : {transacao[2]}")
    print(f"Saldo:\t\tR$ {saldo:.2f}")

def main():

    MENU = """ 

    [d] Depositar
    [s] Sacar
    [e] Extrato 
    [q] Sair

    """

    saldo = 1000
    extrato = []
    contador = 8
    LIMITE_DIARIO_TRANSACAO = 10

    print ("Olá, seja bem vindo ao LeleBank")

    while True: 
        print("=" * 50)
        print(MENU)
        opcao = input("Informe qual opção você deseja:")    
        
        if opcao.lower() == "d":
            novo_saldo, novo_contador = executa_deposito(extrato, contador, LIMITE_DIARIO_TRANSACAO)
            saldo += novo_saldo
            contador += novo_contador

        elif opcao.lower() == "s":
            novo_saldo, novo_contador = executa_saque(
                saldo=saldo,
                extrato=extrato, 
                contador=contador, 
                limite_diario_transacao=LIMITE_DIARIO_TRANSACAO
                )
            saldo += novo_saldo
            contador += novo_contador              

        elif opcao.lower () == "e":
            executa_extrato(saldo, extrato=extrato)

        elif opcao.lower() == "q":
            print("\33[2;33;44mObrigada por ser cliente LeleBank, tenha um bom dia!\33[m")
            break

        else:
            print("Opcão inválida, tente novamente!")

main()

