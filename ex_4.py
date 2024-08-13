'''4. Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 6,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21'''

def converter(real):
    '''Converter Real para várias Moeadas diferentes'''
    
    taxas = {
        'Dólar Americano': 4.91,
        'Peso Argentino': 0.02,
        'Dólar Australiano': 3.18,
        'Dólar Canadense': 3.64,
        'Franco Suiço': 6.42,
        'Euro': 5.36,
        'Libra esterlina': 6.21,
    }
    
    for moeda, taxa in taxas.items():
        valor = real / taxa
        print(f'Você pode comprar {valor:.2f} {moeda}')
                 
        
dinheiro = float(input('Quanto de dinheiro em R$ você tem? '))

converter(dinheiro)

