# Funções:

# Declarando uma função sem aprametro:
def hello():
    print('Olá, Mundo!')


hello()
print()


# Declarando uma função com parametro que calcula média de três notas:
def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media


nota = calcula_media(8.5, 4.9, 10)
print(f'Média: {nota}')
print()


# Funções recursivas:

def funcaoRecursiva(numero):
    if (numero != 1):
        funcaoRecursiva(numero - 1)
    print(numero)


print("Testando a função recursiva:")
funcaoRecursiva(10)
print()


# Funções II

# Funções com varios parametros: Quando utilizamos um * em parametros, quer dizer que posso passar varios argumentos e esses argumentos são armazenados em
# uma tupla().
def calcula_media1(*args):
    soma = sum(args)
    media = soma / len(args)
    return media


print(f'Média de varios parametros: {calcula_media1(10, 5, 8, 9, 10, 7, 6, 2)}')
print()

# Funções com varios parametros: Quando utilizamos dois ** em parametros, quer dizer que posso passar varios argumentos e esses argumentos são armazenados em
# um dicionario().
def print_info(**kwargs):
    print(kwargs, type(kwargs))


print_info(nome='Diego', sobrenome='Dantas')
