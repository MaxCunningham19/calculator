from validation import validateExpression
from testing_kit import Test


def test_validateExpression() -> None:
    tests = [Test("Simple Expr", [1, '+', 1], None),
             Test("Simple Expr2", [12, '/', 4], None),
             Test("Brackets", ['(', 1, '+', 1, ')', '+', 2], None),
             Test("Multiple Operations", [1, '+', 2, '*', 3, '/', 7, '-', 9], None),
             Test("Multi Digits", [1, '*', 21, '-', 190, '/', 8, '+', 346759], None),
             Test("More Numbers", [1, 1, '+', 1], "Error: two numbers in a row: 1 and 1"),
             Test("More Operations", [1, '+', '*', 2], "Error: two operators in a row: + and *"),
             Test("Operator first", ['*', 45], "Error: starts with operator"),
             Test("Operator last", [45, '/'], "Error: ends with operator"),
             Test("Left bracket error", ['(', 56, '+', 45], "Error: open left bracket"),
             Test("Right bracket error", [56, '+', 45, ')'], "Error: open right bracket")]

    has_failure = False
    for t in tests:
        result = validateExpression(t.input)
        if result != t.output:
            print("Test", t.name, "failed - Expected:", t.output, "Got:", result)
            has_failure = True
    assert(not has_failure)


class inp:
    def __init__(self,exp,i):
        self.exp = exp
        self.i = i
