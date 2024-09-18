'''Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.'''

idade = int(input('Digite sua idade: '))

if idade < 0:
    print('Idade Inválida.')
elif idade < 12:
    print('Você é uma criança.')
elif idade < 18:
    print('Você é um adolescente.')
elif idade < 60:
    print('Você é adulto.')
else:
    print('Você é idoso.')
    