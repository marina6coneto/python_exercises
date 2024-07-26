'''Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.'''

from datetime import datetime

while True:
    try:       
        ano_nascimento = int(input('Digite o ano do seu nascimento: '))
        if ano_nascimento > datetime.now().year:
            print('Digite um ano válido')
        else:
            break
    except ValueError:
        print('Digite um ano válido')
        

ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade < 0:
    print('O ano de nascimento informado é inválido.')
else:
    print(f'Você tem {idade} ano(s)')
