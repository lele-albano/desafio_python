# Desafio Sistema Bancário

## Desafio 1: Conta Bancária

### Implementar sistema bancário:
- [x] Depositar
- [x] Sacar
- [x] Extrato
- [x] Sair

### Operação Depósito
- [x] Depositar apenas valores POSITIVOS
- [x] Populei a lista extrato com depósitos
- [x] Todos os depósitos devem ser exibidos no extrato (usando for/in)

### Operação Saque
- [x] Limite de Saque = 3/dia
    Se lista contem 3 números negativos print "Excedeu o limite de saque diário"

- [x] Limite_Diario = 500/saque
    Se saque > 500 print "Valor de saque proibido"
    Se soma dos saques da lista for > 1500 print "Valor total diario excedido"

- [x] Se saldo < valor_de_saque
    "Saldo insuficiente"

- [x] Para que todos os saques fossem exibidos no extrato, populei a lista de extrato com saque

### Operação Extrato
- [x] Listar todos os saldos e saques realizados

- [x] Exibir saldo da conta

- [x] Extrato em branco (sem movimentações) // usando operador de igualdade ==
    "Não foram realizadas movimentações."

- [x] O valor deve ser expresso da seguinte forma: R$xxx.xx.

## Desafio 2: Data e Hora

- [x] Limite de transações por dia = 10
- [x] O alerta tem que ser exibido se o número de transações do dia ultrapassar o limite
- [x] Mostrar no extrato data e hora das transações.

## Desafio 3: Funções

- [x] Modularizar saque, depósito e extrato em funções. 
- [] Função: cadastrar usuário (cliente).
    - [] Cadastrar nome, data de nascimento, CPF e endereço.
        - [] Endereço string com formato logradouro, nº, bairro, cidade/sigla do estado.
        - [] CPF apenas numeros.
        - [] Proibido 2 usuários com o mesmo CPF.
- [] Função: cadastrar conta bancária vinculada ao usuário.
    - [] A conta é composta por: agência, número da conta e usuário.
        - [] Numero da conta sempre iniciada por 1
        - [] Agência fixa em 0001
        - [] Usuário pode ter mais de 1 conta
        - [] Cada conta pertence a apenas 1 usuario

### Saque (keyword only)
- [x] Argumentos: saldo, valor, extrato, limite, numero_saques e limite_saques.
- [x] Retorno: saldo e extrato.

### Depósito (positional only)
- [x] Argumentos: saldo, valor, extrato.
- [x] Retorno: saldo e extrato.

### Extrato (keyword and positional)
- [x] Argumentos posicionais: saldo.
- [x] Argumentos nomeados: extrato.
