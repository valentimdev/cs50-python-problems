from bank import value


def test_hello():
    assert value("Hello world") == 0
    assert value("hello") == 0


def test_h():
    assert value("hahaha") == 20
    assert value("HOhoho") == 20


def test_others():
    assert value("Baby") == 100
