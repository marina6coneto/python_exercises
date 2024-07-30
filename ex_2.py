'''Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.
'''

medias = []

for i in range(0, 5):
    notas = []
    for j in range(0, 4):
        nota = float(input(f'Nota {j+1} do aluno {i+1}: '))
        notas.append(nota)
        
    media = sum(notas) / 4
    medias.append(media)
    
alunos_aprovados = [media for media in medias if media >= 7]
print(len(alunos_aprovados))
    
