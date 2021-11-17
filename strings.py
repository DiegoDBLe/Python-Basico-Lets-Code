# Strings I
empresa = "Let's code"
print(empresa)
print()

frase = "O Professor Pietro da Let's Code disse: \"Hoje a pizza é por minha conta\""
print(frase)
print()

#Método len():

tamanho = len(frase)
print("A frase possui", tamanho, "caracteres")

# Fatiando uma String:
empresa1 = 'Google'
print(f'Mostrando a letra na posição 0 do nome {empresa1}:  {empresa1[0]}')

print(f'Mostrando as três primeiras letras do nome {empresa1}:  {empresa1[:3]}')

# Métodos split para String's:
nomes_cidades = 'São Paulo, Belo Horizonte, Rio de Janeiro, Brasilia'
print(nomes_cidades[0]) # Antes do método split(', ') ele retorna somente a primeira letra 's' da cidade de são paulo
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)
print(nomes_cidades[0]) # Usando o método split ele retorna o nome da cidade de São Paulo
print(nomes_cidades[1])
print()

# Método strip():
cabecalho = '               MENU PRINCIPAL          '
# Sem o método strip():
print(f'Sem o método strip(): {cabecalho}')
# Com o método strip():
print(f'Com o método strip(): {cabecalho.strip()}')
print()

# Métodos: title(), capitalize(), lower(), upper():
cidade = 'rIo dE JaNeiRo'
print(f'Usando o Método title(): {cidade.title()}')
print(f'Usando o Método capitalize(): {cidade.capitalize()}')
print(f'Usando o Método lower(): {cidade.lower()}')
print(f'Usando o Método upper(): {cidade.upper()}')
print()

# Exercicio:
nome_cidade = input('Qual cidade do Brasil é conhecida como cidade maravilhosa?  ').strip()
while nome_cidade.lower() != 'rio de janeiro':
    print('Tenta de novo ai...')
    nome_cidade = input('Qual cidade do Brasil é conhecida como cidade maravilhosa?  ').strip()
print('Boa Campeão!! ')

# Podemos converter strings para listas:
listafrase = list(frase)
print(f'Podemos converter strings para listas: {listafrase}')

# A função join() intercala cada elemento de uma lista com uma string.
stringfinal = '-py'.join(listafrase)
print(stringfinal)
print()


# Usar um join() com uma string vazia é útil para transformar a lista de volta
# em string:
stringfinal = ''.join(listafrase)
print(stringfinal)

# Podemos inserir quebras de linha com '\n'
frase = 'uma\nFRASE'
print(frase)
# Podemos inserir tabulação com '\t'
frase = 'uma\n\tFRASE'
print(frase)
# Para conseguir representar a barra '\', precisamos de 2 barras:
frase = 'uma\\FRASE'
