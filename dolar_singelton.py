from singleton import singleton
from random import randint

@singleton
class Valor_dolar(object):
    def __init__(self, valor):
        self.valor = valor


n = randint(200, 230)
valor = Valor_dolar(n)