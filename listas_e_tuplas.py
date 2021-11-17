# Listas e Tuplas:

# Criando uma Lista:
nomes_paises = ['Brasil', 'Argentina', 'China', 'Canadá', 'Japão']

print(f'Tamanho da lista: {len(nomes_paises)} paieses cadastrados: {nomes_paises}')

# Indexzação base 0:
print(f'O pais no indice 4 é : {nomes_paises[4]}')
# ou
print(f'O pais no indice -1 é : {nomes_paises[-1]}')

# Trocando o pais Japão por Colômbia:
nomes_paises[4] = 'Colômbia'
print(nomes_paises)

# Retornando os paises na posição 1 e 2:
print(f'Retornando os paises na posição 1 e 2: {nomes_paises[1:3]}')

# Retornando os paises na posição 1 até a -1:
print(f'Retornando os paises na posição 1 até a -1: {nomes_paises[1:-1]}')

# Retornando os paises na posição 2 até o final da minha lista:
print(f'Retornando os paises na posição 2 até o final da minha lista: {nomes_paises[2:]}')

# Retornando os paises na posição inicial  até a posição 3:
print(f'Retornando os paises na posição inicial  até a posição 3: {nomes_paises[:3]}')

# Retornando os paises pulando de duas em duas posições:
print(f'Retornando os paises pulando de dois em dois posições: {nomes_paises[::2]}')

# Invertendo a ordem da lista:
print(f'Invertendo a ordem da lista: {nomes_paises[::-1]}')

# Checando se um pais está na lista: Retorno boolean:
print('Checando se o pais Brasil está na lista: Retorno boolean:', 'Brasil' in nomes_paises)
print()

# Criando uma nova lista vazia:
lista_capitais = []
print('Criando uma nova lista vazia e Adicionando capitais na minha lista vazia:')

# Adicionando elementos na minha lista vazia:
lista_capitais.append('Brasilia')
lista_capitais.append('Buenos Aires')
lista_capitais.append('Pequim')
lista_capitais.append('Bogotá')

print(lista_capitais)

# Adicionando um elemento na minha lista em uma posição especifica. Ex: Paris na posição 2:
print(f"Adicionando um elemento na minha lista em uma posição especifica. Ex: Paris na posição 2: {lista_capitais.insert(2, 'Paris')}")
print(lista_capitais)

# Removendo um pais da lista. No ex: ser Buenos Aires. Removendo pelo nome:
lista_capitais.remove('Buenos Aires')
print(f'Removendo a capital Buenos Aires: {lista_capitais}')

# Método pop que remove pela posiçã do elemento:
removido = lista_capitais.pop(2)
print(f'Removendo a capital {removido} na posição 2: {lista_capitais}')
print()
print()
# Criando uma lista vazia.
listavazia = []

# Criando uma lista com alguns valores.
numeros = [1, 3, 7, 8, 9]

# Listas podem mesclar diferentes tipos de valores.
listamista = [14, "let's code", 0.1, True]

# Acessamos cada elemento da lista através de um índice entre colchetes.
# Os índices começam em 0.
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])

# Listas são mutáveis: podemos alterar o valor de seus itens.
numeros[2] = 5
print(numeros)

# Um jeito inteligente de trabalhar com listas é utilizando loops.
indice = 0
while indice < 5:
    print(f'Um jeito inteligente de trabalhar com listas é utilizando loops: {numeros[indice]}')
    indice = indice + 1

print()
print()

#Outra função útil é lista.append(), que coloca um elemento novo ao final da lista.
animais = []
resposta = 's'
while resposta == 's' or resposta == 'S':
    resposta = input('Deseja adicionar um animal à lista (s/n)? ')
    if (resposta in 'sS'):
        animal = input('Digite o nome do animal: ')
        animais.append(animal) # adiciona o novo animal à lista
print(animais)
print()
print()
# A função lista.remove() deleta um elemento da lista. (mas dá erro se o elemento não existir).
animal = input('Digite o animal a ser deletado da lista: ')
animais.remove(animal)
print(animais)
print()
print()

# Algumas outras funções úteis:

# lista.count() conta quantas vezes um elemento aparece.
jogadores = ['Ronaldo', 'Rivaldo', 'Ronaldo', 'Adriano']
ronaldos = jogadores.count('Ronaldo')
print(jogadores)
print('Quantidade de Ronaldos: ', ronaldos)
print()

# lista.index() busca em um elemento e fala em qual posição ele aparece.
rivaldo = jogadores.index('Rivaldo')
print("Rivaldo está na posição ", rivaldo)
print()

# lista.sort() ordena uma lista.
jogadores.sort()
print("jogadores em ordem alfabética: ", jogadores)
print()

# As funções max(lista) e min(lista) obtém, respectivamente, o maior e o menor valor.
digitos = [3, 1, 4, 1, 5, 9, 2, 6, 5]
maior = max(digitos)
menor = min(digitos)
print(digitos)
print("Maior = ", maior, "e menor = ", menor)
print()
print()

print(' Criando uma Tupla: ')
# Criando uma Tupla:
nome_estado = 'São Paulo', 'Ceará', 'Rio de Janeiro', 'Rio Grande do Sul'
print(f'Tamanho da tupla: {len(nome_estado)} posições.')

# Atribuindo cada elemento da tupla ha uma variavel:
s, c, r, rio = nome_estado
print(s, c,)

# Uma tupla é uma coleção de objetos que lembra muito as listas.

# Ao invés de colchetes, usamos parênteses para declarar as tuplas:
numeros = (1,2,3,5,7,11)

# Podemos declarar sem parênteses também:
numeros_sem_parenteses = 1, 2, 3, 5, 7, 11

# Para acessar um valor, utilizamos a mesma sintaxe das listas:
print(numeros[4])
print(type(numeros))

'''
Porém, tuplas são imutáveis: não é possível adicionar ou modificar valores.
Descomentar a linha abaixo provocará erro de execução:
'''
# numeros[4] = 8

# Podemos gerar uma tupla a partir de uma lista...
lista1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
tupla1 = tuple(lista1)
print(tupla1)

# ...ou uma lista a partir de uma tupla:
tupla2 = [1, 6, 1, 8]
lista2 = list(tupla2)
print(lista2)

# Também pode-se usar o unpacking com uma tupla:
a, b, c, d, e, f = numeros # "desempacota" a tupla numeros
print("O primeiro vale:", a, "e o ultimo vale:", f)
