'''Faça um programa que lê três números inteiros e os mostra em ordem
crescente.'''

numeros = input('Digite 3 números separados por virgulas: ')
lista_numeros = numeros.split(',')
num1 = int(lista_numeros[0])
num2 = int(lista_numeros[1])
num3 = int(lista_numeros[2])

if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(f'Números em ordem crescente: {num1}, {num2}, {num3}')
    else:
        print(f'Números em ordem crescente: {num1}, {num3}, {num2}')
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(f'Números em ordem crescente: {num2}, {num1}, {num3}')
    else:
        print(f'Números em ordem crescente: {num2}, {num3}, {num1}')
else:
    if num1 <= num2:
        print(f'Números em ordem crescente: {num3}, {num1}, {num2}')
    else:
        print(f'Números em ordem crescente: {num3}, {num2}, {num1}')
