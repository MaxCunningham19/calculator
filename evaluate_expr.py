def isNumber(char):
    if 48 <= ord(char) <= 57:
        return True
    return False


def convertToList(input_to_calc: str):
    # no_space = input_to_calc.replace(" ", "")
    last_num = False
    expr = []
    for char in input_to_calc:
        if isNumber(char):
            if last_num:
                expr[-1] = expr[-1] * 10 + (ord(char)-48)    # convert string to number, add onto end of number in list
            else:
                last_num = True
                expr.append(ord(char)-48)     # convert from string to number and add to list
        elif char == ' ':
            last_num = False
        else:
            last_num = False
            expr.append(char)
    return expr


def applyOp(val1, op, val2):
    if op == "+":
        return val1 + val2
    elif op == "-":
        return val1 - val2
    elif op == "*":
        return val1 * val2
    elif op == "/":
        return val1 / val2
    elif op == "^":
        return val1 ^ val2      # shouldn't be any other possible values as validChar function handles those cases


def getPrecedence(token):
    if token == "+":
        return 1
    elif token == "-":
        return 1
    elif token == "*":
        return 2
    elif token == "/":
        return 2
    elif token == "^":
        return 3        # shouldn't be any other possible values as validChar function handles those cases


def act(val_stack, op_stack):
    op = op_stack.pop()
    val2 = val_stack.pop()
    val1 = val_stack.pop()
    res = applyOp(val1, op, val2)
    val_stack.append(res)


def evaluatePostfix(expr):
    val_stack = []
    op_stack = []
    for token in expr:
        if isinstance(token, int):
            val_stack.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while op_stack[-1] != "(":
                act(val_stack, op_stack)
            op_stack.pop()  # discard "("
        else:
            while len(op_stack) != 0 and getPrecedence(op_stack[-1]) >= getPrecedence(token):
                act(val_stack, op_stack)
            op_stack.append(token)

    while len(op_stack) != 0:
        act(val_stack, op_stack)

    return val_stack.pop()


if __name__ == "__main__":
    print("Welcome to simple calculator")
    stuff_to_calculate = input("Enter your calculation: ")
    if isValidChars(stuff_to_calculate):
        test = convertToList(stuff_to_calculate)
        result = evaluatePostfix(test)
        print(result)
    else:
        print("error")
