import importlib
import pytest

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary


def test_convert_10():
    assert decimal_to_binary(10) == "1010"


def test_convert_0():
    assert decimal_to_binary(0) == "0"


def test_convert_1():
    assert decimal_to_binary(1) == "1"


def test_convert_5():
    assert decimal_to_binary(5) == "101"


def test_convert_8():
    assert decimal_to_binary(8) == "1000"


def test_convert_large_number():
    assert decimal_to_binary(100) == "1100100"



def test_negative_number_raises_value_error():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)