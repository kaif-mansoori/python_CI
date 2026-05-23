from calculator import add,subtract,multiply,divide

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert subtract(10, 5) == 5

def test_mul():
    assert multiply(2, 5) == 10

def test_div():
    assert divide(10, 2) == 5