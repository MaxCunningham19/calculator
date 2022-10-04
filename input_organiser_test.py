import input_organiser as io
from testing_kit import Test


def test_getPrecidence() -> None:
    tests = [Test("Multi", '*',2),
             Test("Sub",'-',1),
             Test("Add",'+',1),
             Test("Div",'/',2),
             Test("Pow",'^',3),
             Test("No OP",' ', None)]


def test_isValidChars() -> None:
    tests = [Test("addition","1+1",True),
            Test("multiplication","1x2",True),
            Test("subtraction","1-1",True),
            Test("division","1%1",True),
            Test("all numbers","1+2+3+4+5+6+7+8+9+0",True),
            Test("bad input correct chars","6+",True),
            Test("brackets","(1+1)+1",True),
            Test("letters","a+b",False),
            Test("weird chars","$#^*.,",False)]

    fails = []
    for t in tests:
        result = io.getPrecedence(t.input)
        if t.output != result:
            fails.append(t)

            print("Test", t.name, "Fails Expected:", t.output, "Got:", result)
    print("isNumber Test Complete...")
    assert (len(fails) == 0)


