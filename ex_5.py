'''5. Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.'''

def contar_vogais(frase):
    vogais = 0
    for letra in frase:
        if letra in 'aeiou':
            vogais += 1
    return vogais
        
frase = input('Digite uma frase para contarmos as vogais: ').lower()

print(contar_vogais(frase))