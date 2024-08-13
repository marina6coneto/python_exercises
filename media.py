def calcular_media(valores):
    if not valores:
        return 0 
    soma = sum(valores)
    tamanho = len(valores)
    media = soma / tamanho
    return media

continuar = True
valores = []

while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    if valor.lower() == 'ok':
        continuar = False
    else:
        try:
            valor_numero = float(valor)  
            valores.append(valor_numero)  
        except ValueError:
            print("Por favor, digite um número válido ou 'ok' para calcular.")

media = calcular_media(valores)
print(f'A média calculada para os valores {valores} foi de {media}')
