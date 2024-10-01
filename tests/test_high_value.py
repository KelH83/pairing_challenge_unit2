from lib.high_value import *

def test_creates_instance():
    get_high = HighValue(2, 3)
    assert isinstance(get_high, HighValue)
    assert get_high.value_first == 2
    assert get_high.value_second == 3

def test_get_highest_first_highest():
    get_high = HighValue(3,2)
    assert get_high.get_highest() == "First value is higher"

def test_get_highest_second_highest():
    get_high = HighValue(2,3)
    assert get_high.get_highest() == "Second value is higher"

def test_get_highest_equal():
    get_high = HighValue(2,2)
    assert get_high.get_highest() == "Values are equal"

def test_add_selection_first():
    get_high = HighValue(2,3)
    get_high.add(2, 'first')
    assert get_high.value_first == 4

def test_add_selection_second():
    get_high = HighValue(2,3)
    get_high.add(2, 'second')
    assert get_high.value_second == 5