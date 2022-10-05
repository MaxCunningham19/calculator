import input_organiser as io
from testing_kit import Test


def test_getPrecedence() -> None:
    tests = [Test("Multi", '*', 2),
             Test("Sub", '-', 1),
             Test("Add", '+', 1),
             Test("Div", '/', 2),
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
    tests = [Test("addition", "+", 16),
             Test("multiplication", "*", 48),
             Test("subtraction", "-", 8),
             Test("division", "/", 3)]

    fails = []
    for t in tests:
        result = io.applyOp(12, t.input, 4)
        if t.output != result:
            fails.append(t)

            print("Test", t.name, "Fails Expected:", t.output, "Got:", result)
    print("isNumber Test Complete...")
    assert (len(fails) == 0)


def test_calculate():
    tests = [Test("Simple Exp No Space", "1+1", 2),
             Test("Simple Exp w/ Space", "1 + 1", 2),
             Test("Brackets", "(1 + 1) + 2", 4),
             Test("Multiple Operations", "1 + (2 * 3) / 6 - 9", -7),
             Test("Double Digits", "10 + 54", 64),
             Test("Multi Digits", "1 * 21 - 190/19 + 346759", 346770)]

    fails = []
    for t in tests:
        result = io.calculate(t.input)
        if t.output != result:
            fails.append(t)

            print("Test", t.name, "Fails Expected:", t.output, "Got:", result)
    print("isNumber Test Complete...")
    assert (len(fails) == 0)
