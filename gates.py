'''
===========
PYLOGIC v1.0.0
===========

A simple module for simulating Boolean logic operations.
'''

class BinaryNum:
    def __init__(self, usr_num=0, bits=32):
        '''
        Create a binary number.
        '''
        self._usr_num = usr_num
        self.bits = bits
        self._usr_str = str(self._usr_num)
        
        # Check for errors
        if not isinstance(self._usr_num, (int, float)):
            raise TypeError('Number must be binary')
        if len(self._usr_str) > self.bits:
            raise ValueError('Less bits than length of inputted value')
        
        # Set numeric value
        self.__value = ''
        self.__value += '0' * (self.bits - len(self._usr_str))
        self.__value += str(self._usr_num)
    
    def __str__(self):
        return self.value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, num):
        raise Exception('Cannot edit value; use merge() or a logic function')

 
def merge(num1, num2):
    mergednum = num1._usr_str + num2._usr_str
    mergednum = int(mergednum)
    mergedbits = len(str(mergednum))
    return BinaryNum(mergednum, mergedbits)


def one_digit_exceptions(num1):
    usr_int = num1._usr_num
    usr_str = str(usr_int)
    
    # Base exceptions
    if not isinstance(num1, BinaryNum):
        raise Exception('Input must be a BinaryNum')
    if len(usr_str) != 1:
        raise Exception('Input must be 1 digit')
 
 
def NOT(num1):
    one_digit_exceptions(num1)
    return BinaryNum(1 - num1._usr_num, num1.bits)


def OR(num1, num2):
    one_digit_exceptions(num1)
    one_digit_exceptions(num2)
    combined = num1._usr_str + num2._usr_str
    if '1' in combined:
        return BinaryNum(1, max(num1.bits, num2.bits))
    else:
        return BinaryNum(0, max(num1.bits, num2.bits))


def NOR(num1, num2):
    return NOT(OR(num1, num2))


def AND(num1, num2):
    return NOR(NOT(num1), NOT(num2))


def NAND(num1, num2):
    return NOT(AND(num1, num2))


def XOR(num1, num2):
    iter1 = NAND(num1, num2)
    iter2 = OR(num2, num1)
    return AND(iter1, iter2)


def XNOR(num1, num2):
    return NOT(XOR(num1, num2))


def IMPLY(num1, num2):
    one_digit_exceptions(num1)
    one_digit_exceptions(num2)
    if num1._usr_str == '1' and num2._usr_str == '0':
        return BinaryNum(0, max(num1.bits, num2.bits))
    else:
        return BinaryNum(1, max(num1.bits, num2.bits))
    

def NIMPLY(num1, num2):
    return(NOT(IMPLY(num1, num2)))
