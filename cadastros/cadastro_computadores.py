
#Cadastro de Computadores
from computador import Computador
from dados import computadores

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
    novo_computador = Computador(numero, status, valor_computador)
    computadores.append(novo_computador)
    print('Computador cadastrado!')

    while True:
        ver = ver = str(input('Adicionar mais computadores? (S/N): ')).upper()
        if ver == 'S' or ver == 'N':
            break
        else:
            print('Digite apenas S ou N.')
    
    if ver == 'N':
        break
    else:
        pass