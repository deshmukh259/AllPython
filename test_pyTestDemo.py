import pytest
from classCalc import Calcution


def test_calc_mul():
    c = Calcution(1, 2, 3)
    assert c.mul() == 6, "mul is wrong"


@pytest.fixture
def input_value():
   input = 30
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0, "falied"

def test_calc_mul(input_value):
    c = Calcution(1,1,input_value)
    assert c.mul() == input_value , " MULTIFICTION FAILED"

#if __name__ == "__main__":
#    test_calc_mul()
