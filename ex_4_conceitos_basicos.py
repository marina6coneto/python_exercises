'''Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.'''

litros_consumidos = float(input('Quantidade de litros consumidos: '))
distancia = float(input('Distancia percorrida: (km) '))

consumo_medio = distancia / litros_consumidos

print(f'O consumo médio é de {consumo_medio:.2f}km/l.')