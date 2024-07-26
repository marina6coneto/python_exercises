'''Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão'''

num1 = float(input('Digite um número: '))
num2 = float(input('Digite o segundo número: '))
operacao = input('Qual operação? (+, -, /, *) ').strip()

if operacao == '+':
    resultado = num1 + num2
    print(f'O resultado de {num1} {operacao} {num2} = {resultado}')
elif operacao == '-':
    resultado = num1 - num2
    print(f'O resultado de {num1} {operacao} {num2} = {resultado}')
elif operacao == '*':
    resultado = num1 * num2
    print(f'O resultado de {num1} {operacao} {num2} = {resultado}')
elif operacao == '/':
    if num2 == 0:
        print('ERRO: divisão por zero.')
    else:
        resultado = num1 / num2
        print(f'O resultado de {num1} {operacao} {num2} = {resultado}')
else:
    print('Operação inválida.')