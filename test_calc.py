import pytest
from classDemo import Calc


def input():
    return Calc(1, 2, 3)


def test_add():
    c = Calc(1, 2, 3)
    assert c.add() == 6


def test_add_string():
    c = Calc("1", "2", "3")
    with pytest.raises(ValueError):
        c.add() == 4


def test_add_real():
    c = Calc(1.5, 2.3, 3.4)
    with pytest.raises(ValueError):
        c.add() == 4


def test_mul():
    c = Calc(2, 2, 2)
    assert c.mul() == 8


def test_div():
    c = Calc(1, 2, 3)
    assert c.div() >= 0
