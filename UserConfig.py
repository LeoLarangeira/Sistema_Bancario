from main import *
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

    #extrai apenas os números do cpf
    cpf_numeros = ''.join(filter(str.isdigit,cpf))

    dict_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf_numeros,
        'endereco': endereco
    }

    USUARIOS.append(dict_usuario)