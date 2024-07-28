'''Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.
'''
numeros = input('Digite 3 números separados por virgulas: ')
lista_numeros = numeros.split(',')
num1 = int(lista_numeros[0])
num2 = int(lista_numeros[1])
num3 = int(lista_numeros[2])

if num1 == num2 == num3:
    print(f'Todos os números são iguais: {num1}')
elif num1 >= num2 and num1 >= num3:
    print(f'O maior número é {num1}')
elif num2 >= num1 and num2 >= num3:
    print(f'O maior número é {num2}')
else:
    print(f'O maior número é {num3}')
