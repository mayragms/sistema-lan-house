from pessoa import Pessoa
import uuid

class Funcionario(Pessoa):
    def __init__(self, nome, data_nascimento, cpf,cargo):
        super().__init__(nome,data_nascimento,cpf)
        self.cargo = cargo
        self.id_funcionario = str(uuid.uuid4())
