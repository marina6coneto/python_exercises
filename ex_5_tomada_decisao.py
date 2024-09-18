'''Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.'''

#Para que os três segmentos formem um triângulo,
#existe o que conhecemos como condição de existência,
#que é a seguinte: a soma de dois lados é sempre maior que o terceiro lado.

lado_1 = float(input('LADO 1: '))
lado_2 = float(input('LADO 2: '))
lado_3 = float(input('LADO 3: '))

if (lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1):
    if lado_1 == lado_2 == lado_3:
        print('Triângulo equilátero')
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')
else:
    print('Os lados fornecidos não formam um triângulo')