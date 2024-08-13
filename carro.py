'''
    1. Crie uma classe que modele o objeto "carro".
    2. Um carro tem os seguintes atributos: ligado, cor, modelo,
    velocidade.
    3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,
    desacelera.
    4. Crie uma instância da classe carro.
    5. Faça o carro "andar" utilizando os métodos da sua classe.
    6. Faça o carro "parar" utilizando os métodos da sua classe.

'''

class Carro:
    def __init__(self, cor, modelo, velocidade):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade
        
    def liga(self):
        self.ligado = True
    
    def desliga(self):
        self.ligado = False
    
    def acelera(self):
        self.velocidade += 1
    
    def desacelera(self):
        if self.velocidade > 0:
            self.velocidade -= 1
        else:
            print('O carro já está parado')
            
tracker = Carro('Branco', 'Tracker', 5)

tracker.liga() 
print(tracker.ligado) 
 
tracker.acelera()  
print(tracker.velocidade)  

tracker.desacelera()  
print(tracker.velocidade)  

tracker.desliga()  
print(tracker.ligado)  
