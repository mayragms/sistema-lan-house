from cliente import Cliente
from computador import Computador

class Sessao:
    def __init__(self, cliente, computador):
        self.cliente = cliente
        self.computador = computador