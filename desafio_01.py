"""
Sistema bancário simples que permite depósitos, saques e exibição de extrato.
Limitações: 
- Máximo de 3 saques diários
- Limite de saque: R$ 500.00
"""

# Definição de constantes e variáveis globais
SALDO = 0.0  # Saldo da conta bancária
EXTRATO = []  # Lista de transações
LIMITE_SAQUE = 500.0  # Valor máximo por saque
SAQUES_REALIZADOS = 0  # Contador de saques diários
LIMITE_SAQUES_DIARIOS = 3  # Limite máximo de saques por dia

def depositar(quantia):
    """
    Realiza um depósito na conta.
    :param valor: float - Valor a ser depositado
    """
    global SALDO
    if quantia > 0:
        SALDO += quantia
        EXTRATO.append(f"Depósito: R$ {quantia:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")

def sacar(quantia):
    """
    Realiza um saque na conta, respeitando as regras de saldo e limite diário.
    :param valor: float - Valor a ser sacado
    """
    global SALDO, SAQUES_REALIZADOS
    if SAQUES_REALIZADOS >= LIMITE_SAQUES_DIARIOS:
        print("Limite diário de saques atingido.")
    elif quantia > SALDO:
        print("Saldo insuficiente para saque.")
    elif quantia > LIMITE_SAQUE:
        print("O limite máximo por saque é de R$ 500.00.")
    elif quantia > 0:
        SALDO -= quantia
        EXTRATO.append(f"Saque: R$ {quantia:.2f}")
        SAQUES_REALIZADOS += 1
        print("Saque realizado com sucesso!")
    else:
        print("Valor inválido para saque.")

def exibir_extrato():
    """
    Exibe o extrato da conta, incluindo todas as transações e o saldo atual.
    """
    print("\nExtrato da conta:")
    if not EXTRATO:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in EXTRATO:
            print(operacao)
    print(f"Saldo atual: R$ {SALDO:.2f}\n")

# Loop principal do sistema bancário
while True:
    print("\nEscolha uma opção:")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")
    opcao = input("Opção: ")
    
    if opcao == "1":
        valor = float(input("Informe o valor para depósito: "))
        depositar(valor)
    elif opcao == "2":
        valor = float(input("Informe o valor para saque: "))
        sacar(valor)
    elif opcao == "3":
        exibir_extrato()
    elif opcao == "4":
        print("Saindo do sistema bancário.")
        break
    else:
        print("Opção inválida. Tente novamente.")
