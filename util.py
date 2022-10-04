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