# Estruturas Condicionais:
valor_da_passagem = 4.30
valor_da_corrida = float(input('Qual o valor da corrida? R$ '))

if valor_da_corrida <= valor_da_passagem * 5:
    print('Pague a corrida!')
elif valor_da_corrida <= valor_da_passagem * 6:
    print('Aguarde um pouco... Tente novamente em 3 minutos.')
else:
    print('Pegue um ônibus!')