'''Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.'''

calorias_minuto = 5
calorias_hora = calorias_minuto * 60

horas_exercicio_semana = input('Digite a quantidade de horas de exercício físico na semana: ')

try:
    horas_exercicio_semana = float(horas_exercicio_semana)
    if horas_exercicio_semana < 0:
        print('Hora inválida')
    else:
        horas_exercicio_mes = horas_exercicio_semana * 4
        caloria_mes = horas_exercicio_mes * calorias_hora
        print(f'Total de calorias queimada no mês: {caloria_mes}kcal')
except ValueError:
    print('Entrada inválida. Digite um número válido.')
