# Manipulação de Arquivos CSV:
# Importando um biblioteca:
import csv
# Passando o path() para uma variavel e fazendo um for para ler linha por linha. Os valores são separados por virgula, e o retorna de cada valor é uma lista.
with open('C:\\Users\\thyci\\PycharmProjects\\Lets_Code\\Lets_code_python\\python_basics\\brasil_covid.csv..csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    # Mostrando linha por linha:
    # for linha in leitor:
    #     print(linha)

    # Para pular o cabeçalho:
    next(leitor)
    ## Mostrando os valores apenas quando 'novos_casos' for maior que 1. ou seja na posição 2 da lista:
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)

# Fazendo a mesma leitura do arquivo sem importar a biblioteca csv:
with open('C:\\Users\\thyci\\PycharmProjects\\Lets_Code\\Lets_code_python\\python_basics\\brasil_covid.csv..csv', 'r') as csv_file:
    linhas = csv_file.read()
    linhas = linhas.split('\n')
    for linha in linhas:
        linha = linha.split(',')
        print(linha)