import adder


def test_soma_dois_positivos():
    assert adder.soma(1, 1) == 2


def test_soma_dois_negativos():
    assert adder.soma(-1, -1) == -2


def test_soma_nulo():
    assert adder.soma(1, 0) == 1
