from project import add, delete, manage
import pytest

def test_add():
    assert add("John", "1987", "Programmer", "Coding 1", "2022") == 1

def test_delete():
    assert delete("Wakandaforever") == 1

def test_manage():
    with pytest.raises(ValueError):
        manage("Wakandaforever")