from util import convertToList
from validation import validateExpression


def getPrecedence(token):
    if token == "+":
        return 1
    elif token == "-":
        return 1
    elif token == "*":
        return 2
    elif token == "/":
        # shouldn't be any other possible values as validChar function handles those cases.
        return 2


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
        return (
            val1 / val2
        )  # shouldn't be any other possible values as validChar function handles those cases.


def rep(val_stack, op_stack):
    val2 = val_stack.pop()
    if val2 == 0:
        return "Error: divide by zero"
    val1 = val_stack.pop()
    op = op_stack.pop()
    res = applyOp(val1, op, val2)
    val_stack.append(res)
    return None


def evaluateExpression(expr):
    val_stack = []
    op_stack = []
    for token in expr:
        if isinstance(token, int):
            val_stack.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while len(op_stack) != 0 and op_stack[-1] != "(":
                err = rep(val_stack, op_stack)
                if err is not None:
                    return err
            op_stack.pop()  # discard "("
        else:
            while (
                len(op_stack) != 0
                and op_stack[-1] != "("
                and getPrecedence(op_stack[-1]) >= getPrecedence(token)
            ):
                err = rep(val_stack, op_stack)
                if err is not None:
                    return err
            op_stack.append(token)

    while len(op_stack) != 0:
        err = rep(val_stack, op_stack)
        if err is not None:
            return err
    return val_stack.pop()


# calculate assumes that calculation is fully formed and correct
def calculate(stuff_to_calculate: str):
    list_to_calculate = convertToList(stuff_to_calculate)
    validation_result = validateExpression(list_to_calculate)
    if validation_result is None:
        return evaluateExpression(list_to_calculate)
    return validation_result
