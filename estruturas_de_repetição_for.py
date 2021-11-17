# Percorrendo coleções
# O for é um tipo especial de loop feito para percorrer elementos de uma coleção. Acima vimos exemplos usando um while e um contador para percorrer uma lista.
# O for elimina a necessidade de inicializarmos um contador, incrementarmos e verificar a condição de parada. Sintaxe:
# for (variável temporária) in (lista):
#  instruções...

# Criando uma lista e fazendo um for nela ou seja pecorrendo a lista:
nomes_cidade = ['São Paulo', 'Londres', 'Tóquio', 'Paris']
for cidades in nomes_cidade:
    print(f'- {cidades}')

print()

for numeros in enumerate(nomes_cidade):
    print(f'{numeros}')

print()

# Usando for em dicionarios:
# Criando um dicionario:
cidade = {
    'estado': 'São Paulo',
    'cidade': 'São Paulo',
    'população_milhoes': 12.2
}
# chave acessa somente a chave estado, cidade e população_milhoes:
for chave in cidade:
    print(f'{chave}: {cidade[chave]}')


# Função range():
print(list(range(10)))
print((list(range(2, 10))))
print(list(range(2, 10, 2)))


