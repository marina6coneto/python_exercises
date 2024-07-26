'''Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h'''

aviao = 600
carro = 100
onibus = 80 

distancia_viagem = float(input('Digite a distância da sua viagem: (km) '))

if distancia_viagem <= 0:
    print('Digite uma distância positiva')
else:
    tempo_aviao = distancia_viagem / aviao
    tempo_carro = distancia_viagem / carro
    tempo_onibus = distancia_viagem / onibus

    print(f'Tempo de viagem (avião): {tempo_aviao:.2f}h')
    print(f'Tempo de viagem (carro): {tempo_carro:.2f}h')
    print(f'Tempo de viagem (ônibus): {tempo_onibus:.2f}h')