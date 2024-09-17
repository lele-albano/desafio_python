# Desafio Sistema Bancário

Implementar sistema bancário:
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
