from util import isOperator


def validateExpression(expression: []):
    if isOperator(expression[0]):
        return "Error: starts with operator"
    if isOperator(expression[-1]):
        return "Error: ends with operator"

    last_op = ' '
    last_num = ''
    last_bracket = ''
    brackets = 0
    for i in expression:
        if type(i) == int:
            if last_num != '':
                return "Error: two numbers in a row: " + str(last_num) + " and " + str(i)
            if last_bracket == ')':
                return "Error: operator needed after right bracket"
            last_op = ''
            last_num = i
            last_bracket = ''
        elif isOperator(i):
            if last_op != '':
                return "Error: two operators in a row: " + last_op + " and " + i
            if last_bracket == '(':
                return "Error: operator after left bracket"
            last_op = i
            last_num = ''
            last_bracket = ''
        elif i == '(':
            if last_op == '':
                return "Error: operator needed before left bracket"
            brackets += 1
            last_op = ''
            last_num = ''
            last_bracket = '('
        elif i == ')':
            if last_op != '':
                return "Error: operator before right bracket"
            brackets -= 1
            last_op = ''
            last_num = ''
            last_bracket = ')'
        else:
            return "Error: unrecognised character: " + i

    if brackets > 0:
        return "Error: open left bracket"
    if brackets < 0:
        return "Error: open right bracket"

    return None
