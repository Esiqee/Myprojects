from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    with pytest.raises(ValueError):
        jar = Jar(5)
        jar.deposit(8)


def test_withdraw():
    with pytest.raises(ValueError):
        jar = Jar(5)
        jar.withdraw(8)