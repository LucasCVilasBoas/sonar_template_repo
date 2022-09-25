import adder


def test_soma_dois_positivos():
    assert adder.soma(1, 1) == 2


def test_soma_dois_negativos():
    assert adder.soma(-1, -1) == -2


def test_soma_nulo():
    assert adder.soma(1, 0) == 1


def test_soma_dois_nulos():
    assert adder.soma(0, 0) == 0


def test_soma_neg_e_pos():
    assert adder.soma(-1, 1) == 0
