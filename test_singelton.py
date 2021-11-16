from dolar_singelton import Valor_dolar

consulta1 = Valor_dolar()
consulta2 = Valor_dolar()

def test_singelton():
    assert consulta1 == consulta2

def test_valor():
    assert consulta2.valor == consulta1.valor