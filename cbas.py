"""
Computer Boolean Algebra System v1.1
"""

from pylogic.gates import *

operator_info = {
    "L": ["8", "1", NOT],  # NOT
    "•": ["7", "2", AND],  # AND
    "^": ["6", "2", NAND],  # NAND
    "*": ["5", "2", XOR],  # XOR
    "o": ["4", "2", XNOR],  # XNOR
    "+": ["3", "2", OR],  # OR
    "±": ["2", "2", NOR],  # NOR
    ">": ["1", "2", IMPLY],  # IMPLY
}


def is_parenthesis(string):
    return string == "(" or string == ")"


def clean_up_expression(expression: str) -> list:
    output = expression.replace(" ", "")
    for token in expression:
        if (
            not token in operator_info
            and not is_parenthesis(token)
            and not token.isnumeric()
        ):
            raise Exception(f"Invalid expression: {expression}")
        else:
            pass
    return list(output)


def shunting_yard(
    expression: list,
) -> list:  # thx to ModPunchtree to the base of this function :)
    output = []
    operator_stack = []

    for item in expression:
        if item.isnumeric():
            output.append(item)
        elif item == "(":
            operator_stack.append(item)
        elif item in operator_info:
            while (
                operator_stack
                and (operator_stack[-1] != "(")
                and (operator_info[operator_stack[-1]] >= operator_info[item])
            ):
                output.append(operator_stack.pop())
            operator_stack.append(item)
        elif item == ")":
            while operator_stack and operator_stack[-1] != "(":
                output.append(operator_stack.pop())
            operator_stack.pop()
    while operator_stack:
        output.append(operator_stack.pop())
    return output


def solve(expression: list) -> BinaryNum:
    output_stack = []
    for token in expression:
        if token.isnumeric():
            output_stack.append(int(token))
        elif token in operator_info:
            output_stack.append(token)
            operator = output_stack.pop()
            if operator == "L":
                input1 = int(output_stack.pop())
                result = NOT(BinaryNum(input1)).int_value
                output_stack.append(result)
            else:
                input2 = int(output_stack.pop())
                input1 = int(output_stack.pop())
                func = operator_info[operator][2]
                result = func(BinaryNum(input1), BinaryNum(input2)).int_value
                output_stack.append(result)
    return BinaryNum(int(output_stack[0]))


def calculate(expression: str) -> BinaryNum:
    cleaned_expression = clean_up_expression(expression)
    rps_expression = shunting_yard(cleaned_expression)
    return solve(rps_expression)


def reference() -> None:
    print("NOT | AND | NAND | XOR")
    print(" L  |  •  |  ^   |  *\n")
    print("XNOR | OR | NOR | IMPLY | NIMPLY")
    print(" o   | +  |  ±  |   >   |   *L")
