"""
===========
PYLOGIC v1.2.1
===========

A simple module for simulating Boolean logic operations.
Python 3.13.2
"""


class BinaryNum:
    def __init__(self, input_num=0, bits=32):
        """
        Create a binary number.
        """
        self._int_value = input_num
        self._bits = bits
        self._value = str(self._int_value)

        # Check for errors
        if not isinstance(self._int_value, (int, float)):
            raise TypeError("Number must be binary")
        if len(self._value) > self._bits:
            raise ValueError("Less bits than length of inputted value")

        # Set numeric value
        self.__raw_value = ""
        self.__raw_value += "0" * (self._bits - len(self._value))
        self.__raw_value += str(self._int_value)

    def __str__(self):
        return self._value

    def __repr__(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, num):
        raise Exception("Cannot edit value")

    @property
    def raw_value(self):
        return self.__raw_value

    @raw_value.setter
    def raw_value(self, num):
        raise Exception("Cannot edit value; use merge() instead")

    @property
    def bits(self):
        return self._bits

    @bits.setter
    def bits(self, target_bits: int | float):
        if target_bits >= len(self.value) and isinstance(target_bits, int):
            self._bits = target_bits
        else:
            raise ValueError("Target value was not an integer or too small")

    @property
    def int_value(self):
        return self._int_value

    @int_value.setter
    def int_value(self, num):
        raise Exception("Cannot edit value")


def merge(nums: list[BinaryNum], **kwargs: int) -> BinaryNum:
    merged_num = ""
    for value in nums:
        merged_num += value.value
    merged_num = int(merged_num)
    if kwargs:
        merged_bits = kwargs["bits"]
    else:
        merged_bits = len(str(merged_num))
    return BinaryNum(merged_num, merged_bits)


def one_digit_exceptions(num1: BinaryNum):
    usr_int = num1.int_value
    usr_str = str(usr_int)

    # Base exceptions
    if not isinstance(num1, BinaryNum):
        raise Exception("Input must be a BinaryNum")
    if len(usr_str) != 1:
        raise Exception("Input must be 1 digit")


def NOT(num1: BinaryNum) -> BinaryNum:
    one_digit_exceptions(num1)
    return BinaryNum(1 - num1.int_value, num1.bits)


def OR(num1: BinaryNum, num2: BinaryNum) -> BinaryNum:
    one_digit_exceptions(num1)
    one_digit_exceptions(num2)
    combined = num1.value + num2.value
    if "1" in combined:
        return BinaryNum(1, max(num1.bits, num2.bits))
    else:
        return BinaryNum(0, max(num1.bits, num2.bits))


def NOR(num1: BinaryNum, num2: BinaryNum) -> BinaryNum:
    return NOT(OR(num1, num2))


def AND(num1: BinaryNum, num2: BinaryNum) -> BinaryNum:
    return NOR(NOT(num1), NOT(num2))


def NAND(num1: BinaryNum, num2: BinaryNum) -> BinaryNum:
    return NOT(AND(num1, num2))


def XOR(num1: BinaryNum, num2: BinaryNum) -> BinaryNum:
    iter1 = NAND(num1, num2)
    iter2 = OR(num2, num1)
    return AND(iter1, iter2)


def XNOR(num1: BinaryNum, num2: BinaryNum) -> BinaryNum:
    return NOT(XOR(num1, num2))


def IMPLY(num1: BinaryNum, num2: BinaryNum) -> BinaryNum:
    one_digit_exceptions(num1)
    one_digit_exceptions(num2)
    if num1.value == "1" and num2.value == "0":
        return BinaryNum(0, max(num1.bits, num2.bits))
    else:
        return BinaryNum(1, max(num1.bits, num2.bits))


def NIMPLY(num1: BinaryNum, num2: BinaryNum) -> BinaryNum:
    return NOT(IMPLY(num1, num2))
