# Exercicio cadastro de usuario:
import csv
# Criando um cabeçalho:
header = ['Nome: ', 'Sobrenome: ']

# Criando uma lista vazia para armazenar os dados recebidos atraves do input:
dados = []

# Input ao usuario sobre o que deseja fazer:
opc = input('O que deseja fazer?\n\n1 - Para cadastrar usuario: \n0 - Sair\n:')

# loop até que a resposta seja 0 para sair do loop:
while opc != '0':
    nome = input('Qual seu nome ? ')
    sobrenome = input('Qual seu sobrenome ? ')
    # Adicionando as duas variaveis nome e sobrenome na lista vazia.
    dados.append([nome, sobrenome])
    opc = input('O que deseja fazer?\n1 - Para cadastrar usuario: \n0 - Sair\n')

print(dados)

# Criando um arquivo:
with open('cadastro_pesssoas.csv', 'w', newline='') as new_arquivo:
    # Criando um Escritor:
    writer = csv.writer(new_arquivo)
    # Escrevendo o cabeçalho:
    writer.writerow(header)
    # Escrevendo os dados:
    writer.writerows(dados)

# Fazendo a leitura do arquivo criado acima:
with open('cadastro_pesssoas.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)



# DictReader e DictWriter
# Podemos também trabalhar com dicionários, nos quais a primeira linha é lida como a chave e as demais são os respectivos valores:

with open('email.csv', 'r') as emails:
    leitor = csv.DictReader(emails, delimiter=';') #a primeira linha é lida como um cabeçalho
    for linha in leitor:
        print(linha['Login email']) #podemos chamar um valor específico de cada linha pela chave no cabeçallho


with open('names.csv', 'w', newline='') as csvfile:
    chaves = ['first_name', 'last_name'] # definimos o cabeçalho
    writer = csv.DictWriter(csvfile, fieldnames=chaves) # especificamos o cabeçalho

    writer.writeheader() # escrevemos o cabeçalho
    writer.writerow({'first_name': 'Senhor', 'last_name': 'Batata'}) # escrevemos linhas com as chaves e valores
    writer.writerow({'first_name': 'Will', 'last_name': 'Smith'})
    writer.writerow({'first_name': 'Elon', 'last_name': 'Musk'})