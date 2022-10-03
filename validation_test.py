from validation import validateExpression
from testing_kit import Test

def test_validateExpression() -> None:
    tests = [Test("Simple Exp No Space","1+1",True),
             Test("Simple Exp w/ Space", "1 + 1",True),
             Test("Brackets","(1 + 1) + 2",True),
             Test("Multiple Operations", "1 + 2 * 3 / 7^4 - 9", True),
             Test("Double Digits", "10 + 54",True),
             Test("Multi Digits", "1 * 21 - 190/8 + 346759", True),
             Test("More Numbers"," 1 1 + 1", False),
             Test("More Operations", "1 + + 2",False),
             Test("Incorrect Order", "1 + + 1 2", False),
             Test("Incorrect Order 2", " 1 5 *",False),
             Test("Incorrect Order 3", "7 - 1 / - 4 0", False)]

    hasFailure = False
    for t in tests:
        result = validateExpression(t.input)
        if result != t.output:
            print("Test",t.name,"(",t.input,")failed - Expected:",t.output,"Got:",result)
            hasFailure = True
    assert(hasFailure == False)
    