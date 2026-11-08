class LanHouse:
    def __init__(self, nome):
        self.nome = nome
        self.computadores = []

    def adicionar_computador(self, numero, status, valor):
        from computador import Computador

        computador = Computador(numero, status, valor)
        self.computadores.append(computador)