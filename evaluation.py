def getPrecedence(token):
    if token == "+":
        return 1
    elif token == "-":
        return 1
    elif token == "*":
        return 2
    elif token == "/":
        return 2
    # shouldn't be any other possible values as validateExpression function handles those cases.


def applyOp(val1, op, val2):
    if op == "+":
        return val1 + val2
    elif op == "-":
        return val1 - val2
    elif op == "*":
        return val1 * val2
    elif op == "/":
        if val2 == 0:
            return "Error: division by zero"
        return val1 / val2
    # shouldn't be any other possible values as validateExpression function handles those cases.


def divByZero(op, val2) -> bool:
    return val2 == 0 and op == "/"


def performOperation(val_stack, op_stack):
    val2 = val_stack.pop()
    val1 = val_stack.pop()
    op = op_stack.pop()
    if divByZero(op, val2):
        return "Error: division by zero"
    res = applyOp(val1, op, val2)
    val_stack.append(res)
    return None


def calculate(expr):
    val_stack = []
    op_stack = []
    for token in expr:
        if isinstance(token, int):
            val_stack.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while len(op_stack) != 0 and op_stack[-1] != "(":
                err = performOperation(val_stack, op_stack)
                if err is not None:
                    return err
            op_stack.pop()  # discard "("
        else:
            while (
                len(op_stack) != 0
                and op_stack[-1] != "("
                and getPrecedence(op_stack[-1]) >= getPrecedence(token)
            ):
                err = performOperation(val_stack, op_stack)
                if err is not None:
                    return err
            op_stack.append(token)

    while len(op_stack) != 0:
        err = performOperation(val_stack, op_stack)
        if err is not None:
            return err
    return val_stack.pop()
