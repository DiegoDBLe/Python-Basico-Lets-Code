# Estrutura de repetição while:
from time import sleep

cont = 0

while cont < 10:
    cont += 1
    if cont == 1:
        print(f' {cont} Item Limpo!')
    else:
        sleep(1)
        print(f' {cont} Itens Limpos!')

print('Fim!Louça terminada.')
print()

# while True ou seja laço infinito com parada forçada break:
cont1 = 0
while True:
    cont1 += 1
    if cont1 <= 10:
        if cont1 == 1:
            print(f' {cont1} - Item Limpo!')
        else:
            sleep(1)
            print(f' {cont1} - Itens Limpos!')
    else:
        break
print('Fim!Louça terminada.')
print()

# Loop com validação:

texto = input('Digite sua senha: ')

contSenha = 0
while texto != 'LetsCode123':
    contSenha += 1
    texto = input(f'Senha Inválida!  {contSenha}° tentavita, você tem 3 tentativas. \nTente novamente: ')
    if contSenha == 3:
        print('Acesso Bloqueado! Entre em contato com operadora.')
        break
print('Acesso Permitido!')
print()

# Utilizando a palavra reservada continue:
cont4 = 0
while cont4 < 10:
    cont4 += 1
    if cont4 == 1:
        continue
    sleep(1)
    print(f' {cont4} - Itens Limpos!')