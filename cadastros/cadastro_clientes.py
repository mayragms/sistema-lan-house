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
    while True:
        ver = ver = str(input('Adicionar mais ccomputadores? (S/N): ')).upper()
        if ver == 'S' or ver == 'N':
            break
        else:
            print('Digite apenas S ou N.')
    if ver == 'S':
        pass
    else:
        break
