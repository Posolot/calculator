import pytest
from main.calculator import add, subtract, multiply, divide

def test_add():
    assert add(3, 5) == 8
    assert add(-3, 5) == 2
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(5, -3) == 8
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-3, 5) == -15
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 5) == 2
    assert divide(-10, 5) == -2
    assert divide(0, 5) == 0
    with pytest.raises(ValueError):
        divide(5, 0)

# Запуск тестов
if __name__ == "__main__":
    pytest.main([__file__])
