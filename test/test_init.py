from code import increase_all_elements
from code import inc

def test_increase_all_elements():
    assert increase_all_elements([1,2], 3) == [4, 5]

def test_inc():
    assert inc(5) == 6