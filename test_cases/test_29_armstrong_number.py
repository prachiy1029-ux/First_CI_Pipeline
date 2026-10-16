import importlib

module = importlib.import_module("29_armstrong_number")
is_armstrong = module.is_armstrong


def test_armstrong_number_153():
    assert is_armstrong(153) is True


def test_not_armstrong_number_123():
    assert is_armstrong(123) is False


def test_armstrong_number_370():
    assert is_armstrong(370) is True


def test_single_digit_number():
    assert is_armstrong(7) is True


def test_zero():
    assert is_armstrong(0) is True


def test_negative_number():
    assert is_armstrong(-153) is False


def test_armstrong_number_9474():
    assert is_armstrong(9474) is True