class Computador:
    def __init__(self, numero, status, valor_computador):
        self.numero = numero
        self.status = status
        self.valor_computador = valor_computador
    def ocupar(self):
        if self.status == 'disponível':
            self.status = 'ocupado'
            return True
        else:
            print('O computador está ocupado!')
            return False
    def liberar(self):
        if self.status == 'ocupado':
            self.status = 'disponível'
            return True
        else:
            print('O computador está disponível!')
            return False
    def estado(self):
        print(self.status)
        return self.status
