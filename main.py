LIMITE_MAX = 500.00
SAQUE = []
DEPOSITOS = []
EXTRATO = []
SALDO = 0
OPCAO = 0
mensagem = """
    1 - Sacar
    2 - Depositar
    3 - Extrato
"""
def saque(valor):
    global SALDO
    if 0 < valor <= LIMITE_MAX and len(SAQUE) < 3 and SALDO >= valor:
        SALDO -= valor
        SAQUE.append(valor)
        EXTRATO.append(f"SAQUE R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    elif valor > LIMITE_MAX:
        print("Valor de saque excede o limite máximo de R$ 500.00.")
    elif len(SAQUE) >= 3:
        print("Limite diário de saques atingido. Tente novamente amanhã.")
    elif SALDO < valor:
        print("Impossível realizar o saque, saldo insuficiente.")
    else:
        print("Valor de saque inválido.")

def extrato():
    print("Extrato:")
    if not EXTRATO:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in EXTRATO:
            print(movimentacao)
    print(f"Saldo atual: R$ {SALDO:.2f}")

def deposito(valor):
    global SALDO
    if valor > 0:
        SALDO += valor
        DEPOSITOS.append(valor)
        EXTRATO.append(f"DEPÓSITO R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido.")


nome = input("Insira o nome de usuário ")

while(OPCAO == 0):
    print(f'Olá {nome}! O que deseja fazer? ')
    op_menu = int(input(mensagem))

    match op_menu:
        case 1:
            print("Opção de saque selecionada! ")
            valor_saque = float(input("Insira o valor que você deseja sacar: "))
            saque(valor_saque)
        case 2:
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            deposito(valor_deposito)
        case 3:
            extrato()
        case _:
            print("Opção inválida")
    OPCAO = int(input("Deseja continuar? 0 - Sim | 1 Não "))

    if OPCAO == 1:
        print("Muito obrigado por utilizar nossos serviços!")
        break
    elif OPCAO !=1 and OPCAO !=0:
        print("Opção inválida!")
        break
    else:
        continue