'''O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.'''

lista_numeros_pares = []
lista_numeros_impares = []

while True:
    numero = int(input('Digite um número (0 para sair): '))
    
    if numero == 0:
        print(f'Números pares digitados: {lista_numeros_pares}')
        print(f'Números ímpares digitados: {lista_numeros_impares}')
        break
    
    if numero < 0:
        print('Número negativo. Por favor, digite um número positivo.')
    elif numero % 2 == 0:
        lista_numeros_pares.append(numero)
    else:
        lista_numeros_impares.append(numero)
    