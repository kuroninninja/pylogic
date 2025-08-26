import pytest

from gates import *
from cbas import *

one = BinaryNum(1)
zero = BinaryNum(0)


def test_is_binary():
    assert is_binary("101") == True
    assert is_binary("102") == False


def test_bin_type_error():
    with pytest.raises(TypeError):
        mynum = BinaryNum("a")
    with pytest.raises(TypeError):
        mynum = BinaryNum(102)


def test_bin_val_error():
    with pytest.raises(ValueError):
        mynum = BinaryNum(101, 1)


def test_bin_value_change():
    with pytest.raises(Exception):
        mynum = BinaryNum(101)
        mynum.value = 100


def test_bin_raw_value_change():
    with pytest.raises(Exception):
        mynum = BinaryNum(101)
        mynum.raw_value = 100


def test_bin_too_little_bits():
    with pytest.raises(ValueError):
        mynum = BinaryNum(101)
        mynum.bits = 1


def test_bin_not_int_bits():
    with pytest.raises(TypeError):
        mynum = BinaryNum(101)
        mynum.bits = "a"


def test_bin_self_representation():
    mynum = BinaryNum(101, 8)
    assert str(mynum == "101")
    assert repr(mynum == "101")
    assert mynum.raw_value == "00000101"


def test_cannot_edit_int_value():
    with pytest.raises(Exception):
        mynum = BinaryNum(101, 8)
        mynum.int_value = 100


def test_bits_setter():
    mynum = BinaryNum(101, 8)
    target_bits = 32
    mynum.bits = target_bits
    assert mynum.bits == target_bits


def test_merge():
    num1 = BinaryNum(101)
    num2 = BinaryNum(10)
    assert merge([num1, num2]).int_value == BinaryNum(10110).int_value
    assert merge([num1, num2]).bits == 5
    assert merge([num1, num2], bits=30).bits == 30


def test_one_digit_exceptions():
    with pytest.raises(Exception):
        one_digit_exceptions("Hello World")
    with pytest.raises(Exception):
        one_digit_exceptions(BinaryNum(10001))


def test_not():
    assert NOT(BinaryNum(1)).int_value == 0


def test_or():
    assert OR(zero, zero).int_value == zero.int_value
    assert OR(zero, one).int_value == one.int_value
    assert OR(one, zero).int_value == one.int_value
    assert OR(one, one).int_value == one.int_value
