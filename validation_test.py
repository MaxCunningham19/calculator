from validation import validateExpression,findEndOfNumber
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
             Test("Incorrect Order 2", " 1 5 *",(False,3)),
             Test("Incorrect Order 3", "7 - 1 / - 4 0", (False,8))]

    hasFailure = False
    for t in tests:
        result = validateExpression(t.input)
        if result != t.output:
            print("Test",t.name,"failed - Expected:",t.output,"Got:",result)
            hasFailure = True
    assert(hasFailure == False)
    

class inp:
    def __init__(self,exp,i):
        self.exp = exp
        self.i = i


def test_findEndOfNumber():
    tests = [Test("1 Digit", inp("1",0),0),
             Test("2 Digits",inp("10",0),1),
             Test("2 Digits w/ op", inp("10-",0), 1),
             Test("Trips w/Spaces", inp("101 ",0),2),
             Test("No 0 Start",inp("101",1),2),
             Test("Complex", inp(" - 531 124",3),5),
             Test("TwentyOne", inp("21",0),1),
             Test("Twentyone2",inp(" 21 ",1),2)]

    hasFailure = False
    for t in tests:
        result = findEndOfNumber(t.input.exp,t.input.i)
        if result != t.output:
            print("Test",t.name,"failed - Expected:",t.output,"Got:",result)
            hasFailure = True
    assert(hasFailure == False)