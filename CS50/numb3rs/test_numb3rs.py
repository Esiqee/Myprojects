from numb3rs import validate


def test_valid():
    assert validate("1.44.55.222") == True


def test_first_bit():
    assert validate("333.1.1.1") == False


def test_second_bit():
    assert validate("1.333.1.1") == False


def test_third_bit():
    assert validate("1.1.333.1") == False


def test_fourth_bit():
    assert validate("1.1.1.333") == False


def test_str():
    assert validate("cat") == False


def test_toolong():
    assert validate("1.1.1.1.1") == False