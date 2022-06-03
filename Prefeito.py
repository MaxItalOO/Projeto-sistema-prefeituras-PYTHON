class Prefeito:
    def __init__(self, nome, cpf, formacao):
        self._nome = nome
        self._cpf = cpf
        self._formacao = formacao
    
    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def formacao(self):
        return self._formacao