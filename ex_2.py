'''2. Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.'''

def numero_reverso(a):
    parametro_string = str(a)
    inverter_string = parametro_string[::-1]
    numero_invertido = int(inverter_string)
    return numero_invertido

solitica_numero = int(input('Digite um número inteiro: '))

print(numero_reverso(solitica_numero))