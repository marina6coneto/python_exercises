'''3. Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.
Extra: Crie uma terceira, que é um menu para o usuário escolher a
opção desejada, onde esse menu chama a função de conversão
correta.

'''

def converter_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def converter_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def menu():
    while True:
        try:
            temperatura = float(input('Digite uma temperatura que você deseja converter: '))
            break  
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    while True:
        opcao = input('Você quer converter para Celsius ou Fahrenheit? Digite "C" para Celsius ou "F" para Fahrenheit: ').strip().upper()
        if opcao in ('C', 'F'):
            break  
        else:
            print('Opção inválida. Por favor, digite "C" ou "F".')

    if opcao == 'C':
        temp_convertida = converter_celsius(temperatura)
        print(f'{temperatura}°F convertida para Celsius é: {temp_convertida:.2f}°C.')
    else:  
        temp_convertida = converter_fahrenheit(temperatura)
        print(f'{temperatura}°C convertida para Fahrenheit é: {temp_convertida:.2f}°F.')

menu()