from pessoa import Pessoa
import uuid

class Cliente(Pessoa):
    def __init__(self, nome, data_nascimento, cpf):
        super().__init__(nome, data_nascimento, cpf)
        self.id_cliente = str(uuid.uuid4())