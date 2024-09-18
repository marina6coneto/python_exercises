'''Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.'''

user = input('User: ')
password = input('Password: ')

if user == 'admin' and password == 'admin123':
    print('Login successful')
else:
    print('ERROR')