'''Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.'''

salario_bruto = float(input('Digite o salário bruto: R$ '))

imposto = 0.0
salario_base = salario_bruto

if salario_base > 4664.68:
    imposto += (salario_base - 4664.68) * 0.275
    salario_base = 4664.68

if salario_base > 3751.05:
    imposto += (salario_base - 3751.05) * 0.225
    salario_base = 3751.05

if salario_base > 2826.65:
    imposto += (salario_base - 2826.65) * 0.15
    salario_base = 2826.65

if salario_base > 1903.98:
    imposto += (salario_base - 1903.98) * 0.075


salario_liquido = salario_bruto - imposto


print(f'O imposto de renda a ser pago é: R$ {imposto:.2f}')
print(f'O salário líquido é: R$ {salario_liquido:.2f}')


