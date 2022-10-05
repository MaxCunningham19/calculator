operations = {'+', '-', '/', '*'}


def isOperator(char: str) -> bool:
    for op in operations:
        if char == op:
            return True
    return False


ascii_0 = 48
ascii_9 = 57


def isNumber(char: str) -> bool:
    if ascii_0 <= ord(char) <= ascii_9:
        return True
    return False


def convertToList(input_to_calc: str):
    last_num = False
    next_unary = True  # if true, next operator will be applied to number (for negation)
    negate = False
    expr = []
    for char in input_to_calc:
        if isNumber(char):
            if last_num:
                if negate:
                    expr[-1] = expr[-1] * 10 - (ord(char) - 48)  # convert string to number, subtract from end of number in list
                else:
                    expr[-1] = expr[-1] * 10 + (ord(char)-48)    # convert string to number, add onto end of number in list
            else:
                last_num = True
                if negate:
                    expr.append((ord(char)-48)*-1)
                else:
                    expr.append(ord(char)-48)     # convert from string to number and add to list
            next_unary = False  # if operator follows number, it is not unary
            negate = False
        elif char == ' ':
            last_num = False
        elif char == '-' and next_unary:
            negate = not negate
        elif char == ')':
            last_num = False
            expr.append(char)
        else:
            last_num = False
            next_unary = True
            expr.append(char)
    return expr
