from validation import validateExpression
from testing_kit import Test

def test_validateExpression() -> None:
    tests = [Test("Simple Exp No Space","1+1",(True, 3)),
             Test("Simple Exp w/ Space", "1 + 1",(True, 5)),
             Test("Brackets","(1 + 1) + 2",(True, 11)),
             Test("Multiple Operations", "1 + 2 * 3 / 7^4 - 9", (True, 19)),
             Test("Double Digits", "10 + 54",(True,7)),
             Test("Multi Digits", "1 * 21 - 190/8 + 346759", (True, 23)),
             Test("More Numbers","1 1 + 1", (False,2)),
             Test("More Operations", "1 + + 2",(False,4)),
             Test("Incorrect Order", "1 + + 1 2", (False,4)),
             Test("Incorrect Order 2", " 1 5 *",(False,2)),
             Test("Incorrect Order 3", "7 - 1 / - 4 0", (False,8))]

    hasFailure = False
    for t in tests:
        result = validateExpression(t.input)
        if result != t.output:
            print("Test",t.name,"(",t.input,")failed - Expected:",t.output,"Got:",result)
            hasFailure = True
    assert(hasFailure == False)
    