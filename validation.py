
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


operations = {'+', '-', '/', '*', '^'}
def isOperation(char : str) -> bool:
    for op in operations:
        if char == op:
            return True
    return False


ascii_0 = 48
ascii_9 = 57
def isNumber(char : str) -> bool:
    if ascii_0 <= ord(char) <= ascii_9:
        return True
    return False


def findEndOfNumber(exp: str, curI:int) -> int:
    for i in range(curI,len(exp)):
        if not isNumber(exp[i]):
            return i-1
    return len(exp)-1

