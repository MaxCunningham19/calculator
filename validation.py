
def validateExpression(expression: str):
    lastUnitIsOP = True
    for i in range(len(expression)):
        if isOperation(expression[i]):
            if lastUnitIsOP:
                return False, i
            lastUnitIsOP = True
        if isNumber(expression[i]):
            if not lastUnitIsOP:
                return False, i
            lastUnitIsOP = False
            i = findEndOfNumber(expression, i)

    return not lastUnitIsOP, len(expression)


operations = {'+', '-', '/', '*', '^'}
def isOperation(char : str) -> bool:
    for op in operations:
        if char == op:
            return True
    return False


def isNumber(char : str) -> bool:
    if 48 <= ord(char) <= 57:
        return True
    return False


def findEndOfNumber(exp: str, curI:int) -> int:
    for i in range(curI,len(exp)):
        if not isNumber(exp[i]):
            return i - 1
    return len(exp)-1

