# Estruturas Sequenciais:
idade = int(input('Digite sua idade: '))
print(f'Idade {idade}', type(idade))

meses = 12
salario_mensal = float(input('Digite seu salário mensal: R$ '))
gastos_mensal = float(input('Digite seu gasto mensal em média: R$ '))

salario_total = salario_mensal * meses
gastos_total = gastos_mensal * meses

montante_economizado = salario_total - gastos_total
print(f'Total economizado foi de R$ {montante_economizado} ')