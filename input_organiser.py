from util import isNumber

def convertToList(input_to_calc: str):
    # no_space = input_to_calc.replace(" ", "")
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
            negate = True
        elif char == ')':
            last_num = False
            expr.append(char)
        else:
            last_num = False
            next_unary = True
            expr.append(char)
    return expr


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


def act(val_stack, op_stack):
    op = op_stack.pop()
    val2 = val_stack.pop()
    val1 = val_stack.pop()
    res = applyOp(val1, op, val2)
    val_stack.append(res)
    return None


def evaluate(expr):
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
            while len(op_stack) != 0 and op_stack[-1] != '(' and getPrecedence(op_stack[-1]) >= getPrecedence(token):
               err = act(val_stack, op_stack)
               if err != None :
                    return err
            op_stack.append(token)

    while len(op_stack) != 0:
        err = act(val_stack, op_stack)
        if err != None :
            return err
    return val_stack.pop()

# calculate assumes that calulation is fully formed and correct
def calculate(stuff_to_calculate:str):
    test = convertToList(stuff_to_calculate)
    result = evaluate(test)
    return result


