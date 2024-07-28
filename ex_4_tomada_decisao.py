'''Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.'''

aluno = input('Digite o nome do(a) aluno(a): ').strip().title()
nota = float(input('Digite a nota do aluno: '))

if nota < 0 or nota > 10:
    print('Nota inválida')
elif nota >= 7:
    print(f'{aluno} está aprovado(a). Parabéns.')
else:
    print(f'{aluno} está reprovado(a).')

