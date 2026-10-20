from funcionario import Funcionario

funcionarios = []

clientes = []
while True:
    print('---Cadastre um funcionário---')
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
    cargo = input('Cargo: ')
    novo_funcionario = Funcionario(nome, data_nascimento, cpf, cargo)
    funcionarios.append(novo_funcionario)
    print('Funcionário cadastrado!')
    while True:
        ver = ver = str(input('Adicionar mais funcionários? (S/N): ')).upper()
        if ver == 'S' or ver == 'N':
            break
        else:
            print('Digite apenas S ou N.')
    if ver == 'S':
        pass
    else:
        break
