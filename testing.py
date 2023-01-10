from app import equation

def test_positive():
    assert equation(2, 13, 0) == [0.0, -6.5]

def test_equal():
    assert equation(4, 0, 0) == [0.0, 0.0]

def test_negative():
    assert equation(-4, 0, -20) == []