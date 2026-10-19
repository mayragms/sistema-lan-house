from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, data_nascimento, cpf,cargo):
        super().__init__(nome,data_nascimento,cpf)
        self.cargo = cargo
