import evaluation
from testing_kit import Test, runTests


def test_getPrecedence() -> None:
    tests = [
        Test("Addition", "+", 1),
        Test("Subtraction", "-", 1),
        Test("Multiplication", "*", 2),
        Test("Division", "/", 2),
        Test("No OP", " ", None),
    ]

    fails = runTests(tests, evaluation.getPrecedence)
    print("getPrecedence Test Complete...")
    assert len(fails) == 0


def test_applyOp() -> None:
    # applies operation to 12 and 4
    tests = [
        Test("Addition", "+", 16),
        Test("Subtraction", "-", 8),
        Test("Multiplication", "*", 48),
        Test("Division", "/", 3),
    ]
    # applies division with 1 and 0
    zero_test = Test("Divide by zero", "/", "Error: division by zero")

    fails = []
    for t in tests:
        result = evaluation.applyOp(12, t.inp, 4)
        if t.output != result:
            fails.append(t)
            print("Test", t.name, "Fails Expected:", t.output, "Got:", result)

    result = evaluation.applyOp(1, zero_test.inp, 0)
    if result != zero_test.output:
        fails.append(zero_test)
        print("Test", t.name, "Fails Expected:", t.output, "Got:", result)

    print("isNumber Test Complete...")
    assert len(fails) == 0


def test_calculate() -> None:
    tests = [
        Test("Simple Expr", [1, "+", 1], 2),
        Test("Simple Expr2", [12, "/", 4], 3),
        Test("Brackets", ["(", 1, "+", 1, ")", "+", 2], 4),
        Test(
            "Multi Ops",
            ["(", "(", 1, "+", 2, ")", "*", 3, ")", "/", 9, "-", 9],
            -8,
        ),
        Test(
            "Multi Digits",
            [1, "*", 21, "-", 190, "/", 8, "+", 346759],
            346756.25,
        ),
    ]

    fails = runTests(tests, evaluation.calculate)
    assert len(fails) == 0
