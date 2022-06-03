import profile


class Prefeitura:
    def __init__(self, cidade, prefeito):
        self._cidade = cidade
        self._prefeito = prefeito
        self._valor_total_impostos = 0 
        self._empresas = []

    @property
    def cidade(self):
        return self._cidade
    
    @property
    def prefeito(self):
        return (self._prefeito)

    @property
    def valor_total_impostos(self):
        return self._valor_total_impostos

    @property
    def empresas(self):
        return self._empresas
    
    def AdicionarEmpresa (self, Empresa):
        self._empresas.append (Empresa)

    def CalcularImpostosEmpresas(self):
        for cal in self._empresas:
            print(f'EMPRESA: {cal.nome} - IMPOSTOS: {cal.media_lucro_mensal*0.016} - PREFEITURA: {self._cidade}') 
