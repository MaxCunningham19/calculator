from util import isNumber, isOperation


def validateExpression(expression: str):
    lastUnitIsOP = True
    i = 0
    while i < len(expression):
        if isOperation(expression[i]):
            if lastUnitIsOP:
                return False, i
            lastUnitIsOP = True
        if isNumber(expression[i]):
            if not lastUnitIsOP:
                return False, i
            lastUnitIsOP = False
            i = findEndOfNumber(expression, i)
        i = i + 1
    return not lastUnitIsOP, len(expression)


validChars = {'+', '-', '/', '*', '^', '(', ')', ' '}
def isValidChars(input_to_calc: str) -> bool:
    for tmpChar in input_to_calc:
        special = validChars.intersection({tmpChar})
        if len(special) == 0 and not isNumber(tmpChar):
            return False
    return True


def findEndOfNumber(exp: str, curI:int) -> int:
    for i in range(curI,len(exp)):
        if not isNumber(exp[i]):
            return i-1
    return len(exp)-1

