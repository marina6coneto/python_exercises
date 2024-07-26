'''Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.'''

km = float(input('Digite a quantidade de KM que você quer converter: '))

metros = int(km * 1000)
cm = int(metros * 100)
mm = int(cm * 10)

print(f'{km} km é igual a {metros} metros, {cm} centímetros ou {mm} milímetros.')
