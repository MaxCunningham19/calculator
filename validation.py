from util import isNumber, isOperation


# def validateExpression(expression: str):
#     last_unit_is_op = True
#     i = 0
#     while i < len(expression):
#         if isOperation(expression[i]):
#             if last_unit_is_op and expression[i] != '-':
#                 return False, i
#             last_unit_is_op = True
#         elif isNumber(expression[i]):
#             if not last_unit_is_op:
#                 return False, i
#             last_unit_is_op = False
#             i = findEndOfNumber(expression, i)
#         i = i + 1
#     return not last_unit_is_op, len(expression)


def validateExpression(expression: []):
    if isOperation(expression[0]):
        return "Error: starts with operator"

    last_op = ''
    brackets = 0
    for i in expression:
        if type(i) == int:
            last_op = ''
        elif isOperation(i):
            if last_op != '':
                return "Error: two operators in a row: " + last_op + " and " + i
            last_op = i
        elif i == '(':
            brackets += 1
        elif i == ')':
            brackets -= 1
        else:
            return "Error: unrecognised character: " + i

    if brackets > 0:
        return "Error: open left bracket"
    if brackets < 0:
        return "Error: open right bracket"

    return None


validChars = {'+', '-', '/', '*', '^', '(', ')', ' '}


def isValidChars(input_to_calc: str) -> bool:
    for tmpChar in input_to_calc:
        special = validChars.intersection({tmpChar})
        if len(special) == 0 and not isNumber(tmpChar):
            return False
    return True


def findEndOfNumber(exp: str, curI: int) -> int:
    for i in range(curI, len(exp)):
        if not isNumber(exp[i]):
            return i-1
    return len(exp)-1

