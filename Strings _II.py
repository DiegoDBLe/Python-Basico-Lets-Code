# Strings II

# Operador + em string:
cumprimento = 'olá, '
nome = 'Felipe'
print(cumprimento + nome)

# operador * em string:
print(nome * 5)
print()

idade = 35
n_filhos = 2

# Método format():
print('{} tem {} anos e {} filhos'.format(nome, idade, n_filhos))
print()

# Formatando numeros:
preco_gasolina = 3.476
print('O preço da gasolina subiu e está em R$ {:.2f}'.format(preco_gasolina))
print()

# Método f em string:
print(f'{nome} tem {idade} anos e {n_filhos} filhos ')

#
dia = 1
mes = 8
ano = 2019
data1 = '{}/{}/{}'.format(dia, mes, ano)
print(data1)
# Saída: 1/8/2019
# O dia e o mês ocupam apenas 1 espaço

data2 = '{:2d}/{:2d}/{:4d}'.format(dia, mes, ano)
# A opção 'd' significa que o parâmetro é um número inteiro.
print(data2)
# Saída:  1/ 8/2019
# Agora, dia e mês ocupam obrigatoriamente 2 espaços:  1/ 8/2019


# Podemos forçar que os espaços em branco sejam preenchidos com o número 0:
data3 = '{:02d}/{:02d}/{:04d}'.format(dia, mes, ano)
print(data3)
# Saída: 01/08/2019
# Agora sim a data está no formato usual, dd/mm/aaaa: 01/08/2019