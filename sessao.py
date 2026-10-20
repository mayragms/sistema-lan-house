from cliente import Cliente
from computador import Computador
from datetime import datetime

class Sessao:
    def __init__(self, cliente, computador, valor_computador):
        self.cliente = cliente
        self.computador = computador
        self.valor_computador = valor_computador
        self.hora_inicio = None
        self.hora_fim = None
        self.valor_total = None

    def iniciar(self):
        if self.computador.ocupar() == True:
            self.hora_inicio = datetime.now()
            return True
        else:
            print('Não foi possível iniciar a sessão: computador ocupado!')
            return False
    def terminar(self):
        if self.hora_inicio is not None:
            self.hora_fim = datetime.now()
            self.computador.liberar()
        else:
            print('Nenhuma sessão foi iniciada!')
    def calcular_duracao(self):
        if self.hora_inicio is not None and self.hora_fim is not None:
            duracao = self.hora_fim - self.hora_inicio
            return duracao
        else:
            print('A sessão não foi encerrada!')
            return None
        
    def calcular_valor(self):
        duracao = self.calcular_duracao()

        if duracao is not None:
            horas = duracao.total_seconds() / 3600
            self.valor_total = horas * self.computador.valor_computador
            return self.valor_total
    