class Empresa:
    def __init__(self, nome, cnpj, qtd_de_funcionarios, media_lucro_mensal):
        self._nome = nome
        self._cnpj = cnpj
        self._qtd_de_funcionarios = qtd_de_funcionarios
        self._media_lucro_mensal = media_lucro_mensal

    @property
    def nome(self):
        return self._nome

    @property
    def cnpj(self):
        return self._cnpj

    @property
    def qtd_de_funcionarios(self):
        return self._qtd_de_funcionarios

    @property
    def media_lucro_mensal(self):
        return self._media_lucro_mensal


    