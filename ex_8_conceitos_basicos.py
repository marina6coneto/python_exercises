'''Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.'''

salario_hora = float(input('Digite o seu salário por hora: '))
horas_trabalhadas_mes = float(input('Digite a quantidade de horas trabalhadas no mês: '))
salario_mes = salario_hora * horas_trabalhadas_mes

print(f'Seu salário no referido mês é de R${salario_mes:.2f}')