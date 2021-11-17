# Dicionario: Um dicionário é uma coleção, assim como as listas e as tuplas. Porém, enquanto as tuplas eram indexadas por um índice, os dicionários são indexados
# por chaves. Todo elemento em um dicionário possui uma chave e um valor. Chaves tipicamente são strings, valores podem ser qualquer tipo de dado.

# Criando um Dicionario:
dados_cidades = {'Nome': 'São Paulo',
                 'Estado': 'SP',
                 'area KM': 1521,
                 'populações_milhoes': 12.18
                 }
print(dados_cidades)
print()

# Adicionando valores no Dicionario:
dados_cidades['pais'] = 'Brasil'
print(dados_cidades)
print()

# Acessando um valor no dicionario:
print(dados_cidades['Nome'])
print()

# Alterar dados do dicionario:
dados_cidades['area KM'] = 1500
print(dados_cidades)
print()

# Fazendo uma cópia do dicionario:
dados_cidades2 = dados_cidades.copy()
dados_cidades2['Nome'] = 'Santos'
print(dados_cidades)
print(dados_cidades2)
print()

# Atualizando um dicionario:
novos_dados = {
    'populações_milhoes': 15,
    'Fundação': '25/01/1554'
}
dados_cidades.update(novos_dados)
print(dados_cidades)
print()

# Método get() em um valor que não possui no dicionario, retorna none:
print(dados_cidades.get('Prefeito'))
print()

# Método key() retorna uma lista de chaves de um dicionario ou seja transforma um dicionario em lista:
print(dados_cidades.keys())
print()

# Método values() retorna uma lista de valores de um dicionario ou seja transforma um dicionario em lista:
print(dados_cidades.values())
print()

# Método items() retorna uma lista de tuplas (chave, valor) de um dicionario ou seja transforma um dicionario em lista:
print(dados_cidades.items())

# O dicionário é definido pelos símbolos { e }

dicionario = {}

# O dicionário não possui um "append".
# Adicionamos valores diretamente:

dicionario['cat'] = 'gato'
dicionario['dog'] = 'cachorro'
dicionario['mouse'] = 'rato'

print(dicionario)
print(type(dicionario))
print()
'''
Saída:
{'cat': 'gato', 'dog': 'cachorro', 'mouse': 'rato'}
<class 'dict'>
'''

# Dicionários, assim como as listas, são mutáveis:
dicionario['dog'] = 'cão'
print(dicionario)
print()
# Saída: {'cat': 'gato', 'dog': 'cão', 'mouse': 'rato'}

# Podemos criar o dicionário diretamente também:
dicionario2 = {'Curso': 'Python Pro', 'Linguagem':'Python', 'Módulo':2}
print(dicionario2)
print()
# Saída: {'Curso': 'Python Pro', 'Linguagem': 'Python', 'Módulo': 2}

# Podemos utilizar o operador "in" para verificar se uma chave existe:
if 'cat' in dicionario:
    print('cat existe!') # Sim
if 'bird' in dicionario:
    print('bird existe!') # Não
if 'gato' in dicionario:
    print('gato existe!') # Não

'''
Também podemos utilizar as funções .keys() e .values() para obter listas
com apenas as chaves ou apenas os valores do dicionário.
'''
chaves = dicionario.keys()
print(chaves)
print()
# Saída: dict_keys(['cat', 'dog', 'mouse'])

valores = dicionario.values()
print(valores)
print()
# Saída:dict_values(['gato', 'cão', 'rato'])

# Já a função .items(), retorna uma lista de tuplas (chave, valor) de um dicionário

itens = dicionario.items()
print(itens)
print()
# Saída:dict_items([('cat', 'gato'), ('dog', 'cão'), ('mouse', 'rato')])