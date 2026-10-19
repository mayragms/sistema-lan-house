from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, data_nascimento, cpf, id_cliente):
        super().__init__(nome, data_nascimento, cpf)
        self.id_cliente = id_cliente