#Cadastro de Clientes

from cliente import Cliente
clientes = []
while True:
    print('Cadastre um cliente')
    nome = input("Nome: ")
    while True:
        data_nascimento = input("Data de nascimento: ")
        if data_nascimento.isdigit():
            break
        else: 
            print('Digite apenas números!')
    while True:
        cpf = input("CPF: ")
        if cpf.isdigit():
            break
        else:
            print('Digite apenas números!')
    novo_cliente = Cliente(nome, data_nascimento, cpf)
    clientes.append(novo_cliente)
    print('Cliente cadastrado!')
    ver = str(input('Adicionar mais clientes? (S/N): ')).upper()
    if ver == 'S':
        pass
    else:
        break

#Cadastro de Computadores
from computador import Computador

computadores = []

while True:
    while True:
        numero = input('Número do computador: ')
        if numero.isdigit():
            break
        else:
            print('Digite apenas números!')
    status = "disponível"
    while True:
        valor_computador = input('Quanto vai custar a hora? ')
        if valor_computador.isdigit():
            break
        else:
            print('Digite apenas números!')
    print('Computador cadastrado!')
    while True:
        ver = ver = str(input('Adicionar mais ccomputadores? (S/N): ')).upper()
        if ver == 'S' or ver == 'N':
            break
        else:
            print('Digite apenas S ou N.')
    
    if ver == 'N':
        break
    else:
        pass