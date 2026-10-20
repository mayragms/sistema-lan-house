from cliente import Cliente
from computador import Computador
from datetime import datetime
from plano import Plano

class Sessao:
    def __init__(self, cliente, computador, plano=None):
        self.cliente = cliente
        self.computador = computador
        self.plano = plano
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
# Cobrança por hora avulsa
        if duracao is not None and self.plano is None:
            horas = duracao.total_seconds() / 3600
            self.valor_total = horas * self.computador.valor_computador
            return self.valor_total
#Cobrança plano
        if duracao is not None and self.plano is not None:
            horas = duracao.total_seconds()/3600
            
            #Se ultrapassar as horas do plano
            if horas > self.plano.duracao:
                hora_extra = horas - self.plano.duracao
                valor_extra = hora_extra * self.computador.valor_computador
                self.valor_total = self.plano_preco + valor_extra
            
            #Se não ultrapassar
            else:
                self.valor_total = self.plano.preco

            return self.valor_total

        return None
            
        

    