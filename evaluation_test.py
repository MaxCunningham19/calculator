import evaluation as io
from testing_kit import Test


def test_getPrecedence() -> None:
    tests = [Test("Addition", '+', 1),
             Test("Subtraction", '-', 1),
             Test("Multiplication", '*', 2),
             Test("Division", '/', 2),
             Test("No OP", ' ', None)]

    fails = []
    for t in tests:
        result = io.getPrecedence(t.input)
        if t.output != result:
            fails.append(t)

            print("Test", t.name, "Fails Expected:", t.output, "Got:", result)
    print("isNumber Test Complete...")
    assert (len(fails) == 0)


def test_applyOp() -> None:
    # applies operation to 12 and 4
    tests = [Test("Addition", "+", 16),
             Test("Subtraction", "-", 8),
             Test("Multiplication", "*", 48),
             Test("Division", "/", 3)]
    # applies division with 1 and 0
    zero_test = Test("Divide by zero", "/", "Error: division by zero")

    fails = []
    for t in tests:
        result = io.applyOp(12, t.input, 4)
        if t.output != result:
            fails.append(t)
            print("Test", t.name, "Fails Expected:", t.output, "Got:", result)

    result = io.applyOp(1, zero_test.input, 0)
    if result != zero_test.output:
        fails.append(zero_test)
        print("Test", t.name, "Fails Expected:", t.output, "Got:", result)

    print("isNumber Test Complete...")
    assert (len(fails) == 0)


# also tests evaluateExpression
def test_calculate():
    tests = [Test("Simple Exp No Space", "1+1", 2),
             Test("Simple Exp w/ Space", "1 + 1", 2),
             Test("Brackets", "(1 + 1) + 2", 4),
             Test("Multiple Operations", "1 + (2 * 3) / 6 - 9", -7),
             Test("Double Digits", "10 + 54", 64),
             Test("Multi Digits", "1 * 21 - 190/19 + 346759", 346770),
             Test("Error", "45 * / 6", "Error: two operators in a row: * and /")]

    fails = []
    for t in tests:
        result = io.calculate(t.input)
        if t.output != result:
            fails.append(t)

            print("Test", t.name, "Fails Expected:", t.output, "Got:", result)
    print("isNumber Test Complete...")
    assert (len(fails) == 0)
