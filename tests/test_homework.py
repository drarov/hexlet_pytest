import pytest
import copy
from hexlet_pytest.without import set_

@pytest.fixture
def coll():
    return {'a': {'b': {'c': 3}}}

def test_coll1(coll):
    set_(coll, ['a', 'b', 'c'], 4)
    assert coll['a']['b']['c'] == 4

def test_coll2(coll):
    set_(coll, ['x', 'y', 'z'], 5)
    assert coll['x']['y']['z'] == 5

def test_coll3(coll):

    set_(coll, ['a', 'b', 'd'], 7)
    assert coll['a']['b']['d'] == 7
    assert coll['a']['b']['c'] == 3

def test_coll4(coll):
    copied = copy.deepcopy(coll)
    set_(coll, ['a', 'b', 'd'], 7)
    set_(copied, ['a', 'b', 'd'], 7)
    assert copied == coll


