LIMITE_MAX = 500.00
SAQUE = []
DEPOSITOS = []
EXTRATO = []
CONTA_CORRENTE = []
contas_correntes = {}
SALDO = 0
OPCAO = 0
USUARIOS = []
NUMERO_CONTA = 1
AGENCIA = '0001'
mensagem = """
    1 - Sacar
    2 - Depositar
    3 - Extrato
"""
#Criação de usuário

def cadastrar_usuario():
    global USUARIOS
    print("Bem-vindo ao sistema de cadastro de usuário!")
    nome = input("Insira seu nome de usuário: ")
    data_nascimento = input("Insira a data de nascimento do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = input("Digite o endereço do usuário: ")

    for usuario in USUARIOS:
        if usuario['cpf'] == cpf:
            print("Não é possível realizar o cadastro, usuário já cadastrado!")
            return

        # Extrai apenas os números do cpf
    cpf_numeros = ''.join(filter(str.isdigit, cpf))

    dict_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf_numeros,
        'endereco': endereco
    }

    USUARIOS.append(dict_usuario)
    return dict_usuario
def conta_corrente(usuario):
    global NUMERO_CONTA, AGENCIA, CONTA_CORRENTE
    conta = {"agencia": AGENCIA, "numero_conta": NUMERO_CONTA, "usuario": usuario}
    CONTA_CORRENTE.append(conta)
    NUMERO_CONTA += 1
    print(f"Conta corrente criada: Agência {AGENCIA}, Número {conta['numero_conta']}")




def saque(valor, extrato_limite):
    global SALDO
    if 0 < valor <= extrato_limite and len(SAQUE) < 3 and SALDO >= valor:
        SALDO -= valor
        SAQUE.append(valor)
        EXTRATO.append(f"SAQUE R$ {valor:.2f}")
        return print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    elif valor > extrato_limite:
        return print("Valor de saque excede o limite máximo de R$ 500.00.")
    elif len(SAQUE) >= 3:
        return print("Limite diário de saques atingido. Tente novamente amanhã.")
    elif SALDO < valor:
        return print("Impossível realizar o saque, saldo insuficiente.")
    else:
        return print("Valor de saque inválido.")

def extrato(extrato,saldo = SALDO):
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
        return print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        return print("Valor de depósito inválido.")

#Aqui começa o programa
while OPCAO == 0:
    usuario = cadastrar_usuario()
    conta_corrente(usuario)

    print("\nLista de usuários cadastrados:")
    for usuario in USUARIOS:
        print(usuario)

    op_menu = int(input('O que deseja fazer? 0 - Cadastrar novo usuário e conta | 1 - Ir para menu principal: '))
    if op_menu == 1:
        print("Voltando para o menu principal...")
        break
    elif op_menu != 0:
        print("Opção inválida. Saindo do programa...")
        break
while OPCAO == 0:

    op_menu = int(input(mensagem))

    match op_menu:
        case 1:
            print("Opção de saque selecionada! ")
            valor_saque = float(input("Insira o valor que você deseja sacar: "))
            saque(valor = valor_saque, extrato_limite= LIMITE_MAX)
        case 2:
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            deposito(valor_deposito)
        case 3:
            extrato(EXTRATO, saldo = SALDO)
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