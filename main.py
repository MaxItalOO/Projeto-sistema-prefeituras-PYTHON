from Empresa import Empresa
from Prefeitura import Prefeitura
from Prefeito import Prefeito


#LISTAS
Empresas = []
Prefeituras = []
Prefeitos = []



#MENU PRINCIPAL
while True:
    print('##### SISTEMA GOV.BR #####')
    print('1 ► Cadastrar')
    print('2 ► Listar')
    print('3 ► Consultar')
    print('4 ► Relatório impostos')
    print('0 ► Sair')
    menu = int(input('Oque você deseja realizar?\n>> '))



##### 1 ► CADASTRAR #####
    if menu == 1:
        while True:
            print('##### CADASTRAR #####')
            print('1 ► Prefeitura')
            print('2 ► Empresa')
            print('0 ► Voltar')
            menu_cadastrar = int(input('>> '))

        #CADASTRAR NOVA PREFEITURA
            if menu_cadastrar == 1:
                while True:
                    print('#~@~# CADASTRAR PREFEITURA #~@~#')
                    nome_cidade = input('Digite o nome da cidade\n>> ')
                    nome_prefeito = input('Digite o nome do prefeito\n>> ')
                    cpf_prefeito = input('Digite o CPF do prefeito\n>> ')
                    formacao_prefeito = input('Digite a Formação do prefeito\n>> ')

                    prefeito = Prefeito(nome_prefeito, cpf_prefeito, formacao_prefeito)
                    Prefeitos.append(prefeito)
                    prefeitura = Prefeitura(nome_cidade, prefeito)
                    Prefeituras.append(prefeitura)

                    continuar = input('Dejesa adiconar mais uma prefeitura? (s/n)\n>> ')
                    if continuar == 'n':
                        break

        #CADASTRAR NOVA EMPRESA
            if menu_cadastrar == 2: 
                while True:
                    print('#~@~# CADASTRAR EMPRESA #~@~#')
                    nome_empresa = input('Digite o nome\n>> ')
                    cnpj_empresa = input('Digite o CNPJ\n>> ')
                    qtd_de_funcionarios_empresa = input('Digite a quantidade de funcionarios\n>> ')
                    media_lucro_mensal_empresa = int(input('Digite a média de lucro mensal\n>> '))
                    empresa = Empresa(nome_empresa, cnpj_empresa, qtd_de_funcionarios_empresa, media_lucro_mensal_empresa)


                    print(f'Você deseja cadastrar {nome_empresa} à qual prefeitura?')
                    for pre in Prefeituras:
                        print(f'COD {Prefeituras.index(pre)} - CIDADE: {pre.cidade}')
                    prefeitura_empresa = int(input(f'Digite o COD da prefeitura que você deseja associar a {nome_empresa}\n>> '))
                    Empresas.append(empresa)
                    Prefeituras[prefeitura_empresa].AdicionarEmpresa(empresa)

                    continuar = input('Dejesa cadastrar mais uma empresa? (s/n)\n>> ')
                    if continuar == 'n':
                        break

        #VOLTAR PARA O MENU PRINCIPAL
            if menu_cadastrar == 0: 
                break



##### 2 ► LISTAR #####
    elif menu == 2:
        while True:
            print('##### LISTAR #####')
            print('1 ► Prefeituras')
            print('2 ► Empresas')
            print('0 ► Voltar')
            menu_listar = int(input('>> '))

        #LISTAR PREFEITURAS
            if menu_listar == 1:
                for pref in Prefeituras:
                    print(f'COD {Prefeituras.index(pref)} - CIDADE: {pref.cidade} - PREFEITO: {pref.prefeito.nome} - EMPRESAS: {len(pref.empresas)}')

        #LISTAR EMPRESAS
            if menu_listar == 2:
                for emp in Empresas:
                    print(f'EMPRESA: {emp.nome} - CNPJ: {emp.cnpj} - FUNCIONARIOS: {emp.qtd_de_funcionarios} - MÉDIA LUCRO MENSAL: {emp.media_lucro_mensal}')

        #VOLTAR PARA O MENU PRINCIPAL
            if menu_listar == 0:
                break

 

##### 3 ► CONSULTAR #####
    elif menu == 3:
        while True:
            print('##### CONSULTAR #####')
            print('1 ► Prefeitos')
            print('0 ► Voltar')
            menu_consultar = int(input('\n>> '))

        #CONSULTAR DADOS DOS PREFEITOS    
            if menu_consultar == 1:
                for pref in Prefeituras:
                    print(f'COD {Prefeituras.index(pref)} - CIDADE: {pref.cidade} - PREFEITO: {pref.prefeito.nome} - EMPRESAS: {len(pref.empresas)}')
                print('Digite o COD da prefeitura você deseja consultar o prefeito?')
                prefeitura_selecionada = int(input('\n>> '))

                print(f'DADOS DO PREFEITO DE {Prefeituras[prefeitura_selecionada].cidade}!')
                print(f'NOME: {Prefeituras[prefeitura_selecionada].prefeito.nome}')
                print(f'CPF: {Prefeituras[prefeitura_selecionada].prefeito.cpf}')
                print(f'FORMAÇÃO: {Prefeituras[prefeitura_selecionada].prefeito.formacao}\n')

        #VOLTAR PARA O MENU PRINCIPAL
            if menu_consultar == 0:
                break               



##### 4 ► RELATÓRIO IMPOSTOS #####
    elif menu == 4:
        while True:
            print('##### RELATÓRIO IMPOSTOS #####')
            print('1 ► Todas as empresas')
            print('2 ► Todas empresas de uma prefeitura')
            print('0 ► Voltar')
            menu_relatorio_impostos = int(input('>> '))

        #MOSTRAR IMPOSTOS DE TODAS AS EMPRESAS
            if menu_relatorio_impostos == 1:
                if len(Empresas) == 0:
                    print('NÃO EXISTEM EMPRESAS CADASTRADA NO SISTEMA!')
                else:
                    for pref in Prefeituras:
                        pref.CalcularImpostosEmpresas()

        #MOSTRAR IMPOSTOS DE UMA PREFEITURA
            if menu_relatorio_impostos ==2:
                print('##### PREFEITURAS DISPONIVEIS #####')
                if len(Prefeituras) == 0:
                    print('NÃO EXISTEM PREFEITURAS CADASTRADA NO SISTEMA!')
                else:
                    for pref in Prefeituras:
                        print(f'COD {Prefeituras.index(pref)} - CIDADE: {pref.cidade} - EMPRESAS: {len(pref.empresas)}')
                    prefeitura_escolhida = int(input('Digite o COD da prefeitura escolhida:\n>> '))
                    for abc in Prefeituras:
                        Prefeituras[prefeitura_escolhida].CalcularImpostosEmpresas()

        #VOLTAR PARA O MENU PRINCIPAL
            if menu_relatorio_impostos == 0:
                break



##### 5 ► ENCERRAR PROGRAMA  #####              
    if menu == 0:
        break
#MSG DE SUCESSO!!!
print('DEU CERTO!')