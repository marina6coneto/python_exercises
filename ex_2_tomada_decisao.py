'''Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = input('Qual turno você estuda? (M - matutino, V - vespertino, N - noturno): ').strip().upper()

if turno[0] == 'M':
    print('Bom dia')
elif turno[0] == 'V':
    print('Boa tarde')
elif turno[0] == 'N':
    print('Boa noite')
else:
    print('Entrada Inválida')