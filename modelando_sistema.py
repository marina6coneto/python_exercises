'''
    1. O banco Banco Delas é um banco moderno e eficiente, com
    vantagens exclusivas para clientes mulheres.
    Modele um sistema orientado a objetos para representar contas
    correntes do Banco Delas seguindo os requisitos abaixo.
        ● Cada conta corrente pode ter um ou mais clientes como
        titular.
        ● O banco controla apenas o nome, o telefone e a renda
        mensal de cada cliente.
        ● A conta corrente apresenta um saldo e uma lista de
        operações de saques e depósitos.
        ● Quando a cliente fizer um saque, diminuiremos o saldo da
        conta corrente. Quando ela fizer um depósito,
        aumentaremos o saldo.
        ● Clientes mulheres possuem em suas contas um cheque
        especial de valor igual à sua renda mensal, ou seja, elas
        podem sacar valores que deixam a sua conta com valor
        negativo até renda_mensal.
        ● Clientes homens por enquanto não têm direito a cheque
        especial.
    Para modelar seu sistema, utilize obrigatoriamente os conceitos
    "classe", "herança", "propriedades", "encapsulamento" e "classe
    abstrata".

'''
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, saldo=0):
        self._saldo = saldo
        self._operacoes = []

    @property
    def saldo(self):
        return self._saldo

    @property
    def operacoes(self):
        return self._operacoes

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self._saldo += valor
        self._operacoes.append(f"Depósito: +{valor}")
        print(f"Depósito de {valor} realizado com sucesso.")
        
class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @property
    def renda_mensal(self):
        return self._renda_mensal


class ContaCorrente(Conta):
    def __init__(self, cliente, saldo=0):
        super().__init__(saldo)
        self._cliente = cliente

    def sacar(self, valor):
        if isinstance(self._cliente, ClienteMulher):
            limite = self._saldo + self._cliente.renda_mensal
        else:
            limite = self._saldo
        
        if valor <= limite:
            self._saldo -= valor
            self._operacoes.append(f"Saque: -{valor}")
            print(f"Saque de {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente para saque.")

class ClienteMulher(Cliente):
    pass  # Clientes mulheres têm cheque especial

class ClienteHomem(Cliente):
    pass  # Clientes homens não têm cheque especial

# Criação de clientes
cliente1 = ClienteMulher("Marina", "123456789", 3000)
cliente2 = ClienteHomem("Carlos", "987654321", 4000)

# Criação de contas correntes
conta1 = ContaCorrente(cliente1, saldo=1000)
conta2 = ContaCorrente(cliente2, saldo=1000)

# Operações
conta1.depositar(500)
conta1.sacar(4000)  # Permitido devido ao cheque especial
conta2.sacar(1500)  # Não permitido, saldo insuficiente
