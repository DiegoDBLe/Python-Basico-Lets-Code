# Criando um arquivo csv:
import csv

# with open('user_csv', 'w', newline='') as arquivo_user:
#     escritor = csv.writer(arquivo_user)
#     escritor.writerow(['Nome:', 'Sobrenome: ', 'email: ', 'Gênero: '])
#     escritor.writerow(['Diego', 'Dantas', 'ddb.gemail.com', 'Masculino'])


with open('user_csv', 'r', newline='') as arquivo_user:
    leitor = csv.reader(arquivo_user)
    # Mostrando linha por linha:
    for linha in leitor:
         print(linha)