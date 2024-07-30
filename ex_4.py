'''Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.'''

contatos = {
    'Marina': '48 999999999',
    'Felipe': '48 777777777',
    'Valeria': '48 888888888',
    'Nazareno': '48 666666666',
    'Vó Maria': '48 555555555',
    'Vô Nereu': '48 444444444',
    'Nathália': '48 333333333',
}

nome_contato = input('Digite o nome do contato que você quer: ').strip().capitalize()

for nome, telefone in contatos.items():
    if nome_contato == nome:
        print(f'Contato de {nome}: {telefone}')
if nome_contato not in contatos.keys():
     print('Contato não encontrado.')
        

# Outra resolução método get:
# telefone = contatos.get(nome_contato)
# if telefone:
#     print(f'Contato de {nome_contato}: {telefone}')
# else:
#     print('Contato não encontrado.')

# Outra resolução
# if nome_contato in contatos:
#     print(f'Contato de {nome_contato}: {contatos[nome_contato]}')
# else:
#     print('Contato não encontrado.')