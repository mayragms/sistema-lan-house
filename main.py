
from cadastros.cadastro_clientes import cadastrar_cliente
from cadastros.cadastro_funcionarios import cadastrar_funcionario
from cadastros.cadastro_computadores import cadastrar_computador

from dados import clientes, computadores, sessoes, planos
from sessao import Sessao


def iniciar_sessao():
    if not clientes:
        print('\nNão existem clientes cadastrados!')
        return

    if not computadores:
        print('\nNão existem computadores cadastrados!')
        return

    print('\n--- CLIENTES ---')
    for i, cliente in enumerate(clientes):
        print(f'{i + 1} - {cliente.nome}')

    try:
        escolha = int(input('Escolha o cliente: '))
        if escolha < 1 or escolha > len(clientes):
            print('Cliente inválido!')
            return
        cliente = clientes[escolha - 1]

        computadores_disponiveis = [
            computador for computador in computadores
            if computador.status == 'disponível'
        ]

        if not computadores_disponiveis:
            print('Não existem computadores disponíveis!')
            return

        print('\n--- COMPUTADORES DISPONÍVEIS ---')
        for i, computador in enumerate(computadores_disponiveis):
            print(
                f'{i + 1} - Computador {computador.numero} '
                f'| Valor por hora: R$ {computador.valor_computador:.2f}'
            )

        escolha = int(input('Escolha o computador: '))
        if escolha < 1 or escolha > len(computadores_disponiveis):
            print('Computador inválido!')
            return

        computador = computadores_disponiveis[escolha - 1]

        plano = None

        if planos:
            print('\n--- PLANOS ---')
            print('0 - Hora avulsa')

            for i, p in enumerate(planos):
                print(f'{i + 1} - {p.nome} | {p.duracao}h | R$ {p.preco:.2f}')

            escolha = int(input('Escolha o plano: '))

            if escolha < 0 or escolha > len(planos):
                print('Plano inválido!')
                return

            if escolha != 0:
                plano = planos[escolha - 1]

        nova_sessao = Sessao(cliente, computador, plano)

        if nova_sessao.iniciar():
            sessoes.append(nova_sessao)
            print('\nSessão iniciada com sucesso!')
            print(f'Computador {computador.numero}: {computador.status}')

    except ValueError:
        print('Digite uma opção numérica válida!')


def encerrar_sessao():
    sessoes_ativas = [
        s for s in sessoes
        if s.hora_inicio is not None and s.hora_fim is None
    ]

    if not sessoes_ativas:
        print('\nNão existem sessões ativas!')
        return

    print('\n--- SESSÕES ATIVAS ---')

    for i, s in enumerate(sessoes_ativas):
        print(
            f'{i + 1} - Cliente: {s.cliente.nome} '
            f'| Computador: {s.computador.numero}'
        )

    try:
        escolha = int(input('Escolha a sessão para encerrar: '))

        if escolha < 1 or escolha > len(sessoes_ativas):
            print('Sessão inválida!')
            return

        sessao = sessoes_ativas[escolha - 1]

        sessao.terminar()
        valor = sessao.calcular_valor()

        print('\n--- RESUMO DA SESSÃO ---')
        print(f'Cliente: {sessao.cliente.nome}')
        print(f'Computador: {sessao.computador.numero}')
        print(f'Duração: {sessao.calcular_duracao()}')
        print(f'Valor total: R$ {valor:.2f}')
        print(f'Status do computador: {sessao.computador.status}')

    except ValueError:
        print('Digite um número válido!')


def menu():
    while True:
        print('\n========== LAN HOUSE ==========')
        print('1 - Cadastrar cliente')
        print('2 - Cadastrar funcionário')
        print('3 - Cadastrar computador')
        print('4 - Iniciar sessão')
        print('5 - Encerrar sessão')
        print('0 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_cliente()

        elif opcao == '2':
            cadastrar_funcionario()

        elif opcao == '3':
            cadastrar_computador()

        elif opcao == '4':
            iniciar_sessao()

        elif opcao == '5':
            encerrar_sessao()

        elif opcao == '0':
            print('Encerrando o sistema...')
            break

        else:
            print('Opção inválida!')


if __name__ == '__main__':
    menu()
