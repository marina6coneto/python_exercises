'''Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.'''

nome = input('Digite seu nome: ').capitalize().strip()
hobby = input('Qual o seu hobbie favorito? ').lower().strip()
lugar = input('Qual o lugar que você mais gosta? ').capitalize().strip()
sonho = input('Qual o seu sonho? ').lower().strip()

print(f'Olá, {nome}, é ótimo saber que você gosta de {hobby}.' 
      f' Eu também adoro passar tempo na {lugar}.'
      f' Espero que você realize seu sonho de {sonho}.')