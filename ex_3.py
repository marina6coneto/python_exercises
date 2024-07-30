'''Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.'''

preco = {
    'Pão (un)': 1.5,
    'Chocolate': 4.99,
    'Leite (l)': 5.99,
    'Café': 15.99,
    'Ovos (bandeja)': 19.8,
    'Farinha (kg)': 4.6,    
}

carrinho_compras = {
    'Pão (un)': 5,
    'Chocolate': 2,
    'Leite (l)': 12,
    'Café': 2,
    'Ovos (bandeja)': 1,
    'Farinha (kg)': 1,      
}

total_gasto = 0
for item, quantidade in carrinho_compras.items():
    total_gasto += preco[item] * quantidade
    
print(f'O total da compra foi R${total_gasto:.2f}')