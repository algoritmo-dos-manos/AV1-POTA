# Alunos:
# Carlos Fabiany Anselmo da Silva Jr  - 03111398
# Francisco Antonio dos Santos Correa - 03094042
# Igor Pablo da Silva Freitas         - 03220292
# Isabela Zanotto Monteiro            - 03212070


import os

# Modelação da classe:
class Veiculo:
    def __init__(self, tipo, modelo, ano, km, numero_registro):
        
        self.tipo = tipo
        self.modelo = modelo.strip()
        self.ano = int(ano)
        self.km = int(km)
        self.numero_registro = int(numero_registro)
    
    def exibe(self):
        print('+++++++++++++++++++++++++++++++++++++++++++++++')
        print(f'Tipo: {self.tipo}')
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'KM: {self.km}')
        print(f'Numero de Registro: {self.numero_registro}')
        print('+++++++++++++++++++++++++++++++++++++++++++++++')

# Função anonima para limpeza do terminal:
limpar_tela = lambda : os.system('cls' if os.name == 'nt' else 'clear')

# Fução de exibicao do menu principal:
def menu():
    limpar_tela()
    print("...:::: Simulação de registro de carros usados ::::...\n")
    print("Digite o numero da opção desejada:\n")
    print('1 - Adicionar item a lista.')
    print('2 - Exibir lista de itens.')
    print('3 - Realizar pesquisa sequencial atraves do modelo - string. (algoritmo do aluno)')
    print('4 - Realizar pesquisa sequencial atraves do modelo - string. (build-in)')
    print('5 - Realizar pesquisa Binaria atraves do registro - inteiro. (algoritmo do aluno)')
    print('6 - Realizar pesquisa Binaria atraves do registro - inteiro. (build-in)')
    print('7 - Zerar lista de itens.')
    print('0 - Sair\n')
    opcao = input(": ")
    limpar_tela()
    return opcao

# Função para criação da instancia do objeto veiculo:
def registra_veiculo():
    i = True
    while(i):
        tipo = input('Digite o tipo do veiculo. (carro ou moto): ').upper()

        if(tipo == "CARRO" or tipo == "MOTO"):
            limpar_tela()
            print('Tipo registrado com sucesso!!!')
            i = False
        else:
            print('Tipo de veiculo invalido, tente novamente!!!')
    
    modelo = input('Digite o modelo do veiculo. (exp.: gol, celta, CB 300 ...): ').strip().upper()
    limpar_tela()
    print('Modelo adicionado com sucesso!!')
    
    i = True
    while(i):
        ano = input('Digite o ano do veiculo. (entre 1960 e 2021): ')
        if(ano.isnumeric()):
            if(int(ano) >= 1960 and int(ano) <= 2021):
                limpar_tela()
                print('Ano do veiculo registrado com sucesso!!!')
                i = False
            else:
                print('Ano do veiculo fora do limite permitido, tente novamente!!!')
        else:
            print('Uso de caracteres não permitidos!!!')

    i = True
    while(i):
        km = input('Digite a quilometragem do veiculo. (Somente numeros): ')
        if(km.isnumeric()):
            limpar_tela()
            print('Quilometragem registrada com sucesso!!!')
            i = False
        else:
            print('Digito invalido, tente novamente!!!')
    
    i = True
    while(i):
        numero_registro = input('Digite o numero de registro do veiculo. (somente numeros e limite de cinco digitos): ')
        if(numero_registro.isnumeric() and len(numero_registro) <= 5):
            limpar_tela()
            print('Numero de registro salvo com sucesso!!!')
            i = False
        else:
            print('Registro invalido, tente novamente!!!')

    return Veiculo(tipo, modelo, ano, km, numero_registro)

# Inicio da execução do programa principal:
lista_de_veiculos = []
loop = None
while (loop != '0'):
    loop = menu()
    
    # Opção 1 do menu:
    if(loop == '1'):
        lista_de_veiculos.append(registra_veiculo())
        input('Veiculo adicionado com sucesso. pressione ENTER para prosseguir!')
    
    # Opção 2 do menu:
    if(loop == '2'):
        if (lista_de_veiculos == []):
            input("Não existe itens adicionados a lista.\nPressione ENTER para voltar ao menu principal.")
        else:
            for item in range(len(lista_de_veiculos)):
                lista_de_veiculos[item].exibe()
            input('Pressione qualquer tecla para voltar!')
    
    # Opção 3 do menu:
    if(loop == '3'):
        if (lista_de_veiculos == []):
            input("A pesquisa não pode ser realiza pois não exite nenhum item adicionado à lista.")
        else:
            chave_de_pesquisa = input('Informe o nome do modelo a ser pesquisado: ').strip().upper()
            
            # Algoritmo de busca sequencial dos alunos:
            ocorrencias = 0
            for item in range(len(lista_de_veiculos)):
                if(lista_de_veiculos[item].modelo == chave_de_pesquisa):
                    ocorrencias += 1
            if(ocorrencias == 0):
                input('Nenhuma ocorrencia encontrada.')
            else:
                input(f'Foram encontrados o total de {ocorrencias} ocorrencias.')

    # Opção 4 do menu:
    if(loop == '4'):
        if (lista_de_veiculos == []):
            input("A pesquisa não pode ser realiza pois não exite nenhum item adicionado à lista.")
        else:
            chave_de_pesquisa = input('Informe o nome do modelo a ser pesquisado: ').strip().upper()
            lista_de_modelos = []
            for index in range(len(lista_de_veiculos)):
                lista_de_modelos.append(lista_de_veiculos[index].modelo)
            
            # Algoritmo de busca sequencial build-in:
            ocorrencias = lista_de_modelos.count(chave_de_pesquisa)
            input(f'Foram encontrados o total de {ocorrencias} ocorrencias.')

    # Opção 5 do menu:
    if(loop == '5'):
        if (lista_de_veiculos == []):
            input("A pesquisa não pode ser realiza pois não exite nenhum item adicionado à lista.")
        else:
            
            # Algoritmo de ordenação da lista de registro o aluno:
            lista_ordenada_por_registro = []
            for i in range(len(lista_de_veiculos)):
                if (lista_ordenada_por_registro == []):
                    lista_ordenada_por_registro.append(lista_de_veiculos[i])
                else:
                    for j in range(len(lista_ordenada_por_registro)):
                        if (int(lista_ordenada_por_registro[j].numero_registro) >= int(lista_de_veiculos[i].numero_registro)):
                            lista_ordenada_por_registro.insert(j, lista_de_veiculos[i])
                            break
                        elif (j + 1 == len(lista_ordenada_por_registro)):
                            lista_ordenada_por_registro.append(lista_de_veiculos[i])
            
            # Validação de entrada do usuario:
            valor_aceito = True
            while(valor_aceito):
                chave_de_pesquisa = input('Informe o numero de registro a ser pesquisado: ')
                if(chave_de_pesquisa.isnumeric() and len(chave_de_pesquisa) <= 5):
                    valor_aceito = False
                else:
                    print('Valor invalido, digite apenas numeros e o limite de 5 digitos!')

            # Algoritmo de busca binaria:
            inicio = 0
            final = len(lista_ordenada_por_registro) - 1
            ocorrencia = False
            
            while(inicio <= final and not ocorrencia):
                mediana = (inicio + final) // 2
                if(lista_ordenada_por_registro[mediana].numero_registro == int(chave_de_pesquisa)):
                    ocorrencia = True
                else:
                    if(int(chave_de_pesquisa) < lista_ordenada_por_registro[mediana].numero_registro):
                        final = mediana - 1
                    else:
                        inicio = mediana + 1
            if(ocorrencia):
                input(f'O Registro :{chave_de_pesquisa}: foi encontrado na lista.')
            else:
                input('Registro não encontrado!')

    # Opção 6 do menu:
    if(loop == '6'):
        if (lista_de_veiculos == []):
            input("A pesquisa não pode ser realiza pois não exite nenhum item adicionado à lista.")
        else:
            
            lista_ordenada_por_registro = []
            for index in range(len(lista_de_veiculos)):
                lista_ordenada_por_registro.append(lista_de_veiculos[index].numero_registro)
            
            # Algoritmo de ordenação da lista de registro build-in:
            lista_ordenada_por_registro.sort()

            # Validação de entrada do usuario:
            valor_aceito = True
            while(valor_aceito):
                chave_de_pesquisa = input('Informe o numero de registro a ser pesquisado: ')
                if(chave_de_pesquisa.isnumeric() and len(chave_de_pesquisa) <= 5):
                    valor_aceito = False
                else:
                    print('Valor invalido, digite apenas numeros e o limite de 5 digitos!')

            # Inicio da pesquisa binaria:
            inicio = 0
            final = len(lista_ordenada_por_registro) - 1
            ocorrencia = False
            
            while(inicio <= final and not ocorrencia):
                mediana = (inicio + final) // 2
                if(lista_ordenada_por_registro[mediana] == int(chave_de_pesquisa)):
                    ocorrencia = True
                else:
                    if(int(chave_de_pesquisa) < lista_ordenada_por_registro[mediana]):
                        final = mediana - 1
                    else:
                        inicio = mediana + 1
            if(ocorrencia):
                input(f'O Registro :{chave_de_pesquisa}: foi encontrado na lista.')
            else:
                input('Registro não encontrado!')
    
    # Opção 7 do menu:
    if(loop == '7'):
        resposta = input('Você tem certeza que deseja excluir todos os itens da lista?\nDigite (s)sim ou (n)não: ')
        if(resposta == 's'):
            lista_de_veiculos.clear()
            input('Lista zerada com sucesso!!!')
 
print('Fim do programa!!!')