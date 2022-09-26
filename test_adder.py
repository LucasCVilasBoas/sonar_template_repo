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


def test_neg_e_pos():
    assert adder.soma(1, -1) == 0


def test_pos_e_pos():
    assert adder.subtracao(2, 1) == 1


def test_par_ou_impar_com_par():
    assert adder.par_ou_impar(2) == "Par"


def test_par_ou_impar_com_impar():
    assert adder.par_ou_impar(3) == "Ímpar"
