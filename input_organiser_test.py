import input_organiser as io


class Test:
    def __init__(self, name: str, input, output) -> None:
        self.name = name
        self.input = input
        self.output = output


def test_isValidChars() -> None:
    tests = [Test("addition", "1+1", True),
             Test("multiplication", "1*2", True),
             Test("subtraction", "1-1", True),
             Test("division", "1/1", True),
             Test("all numbers", "1+2+3+4+5+6+7+8+9+0", True),
             Test("bad input correct chars", "6+", True),
             Test("brackets", "(1+1)+1", True),
             Test("letters", "a+b", False),
             Test("weird chars", "$#^*.,", False)]

    fails = []
    for t in tests:
        result = io.isValidChars(t.input)
        if t.output != result:
            fails.append(t)
            print("Test", t.name, "Fails Expected:", t.output, "Got:", result)
    print("isValidChar Test Complete...")
    assert (len(fails) == 0)

def test_isNumber() -> None:
    tests = [Test("Zero",'0',True),
             Test("One", '1', True),
             Test("Two", '2', True),
             Test("Three", '3', True),
             Test("Four", '4', True),
             Test("Fives", '5', True),
             Test("Six",'6',True),
             Test("Seven",'7',True),
             Test("Eight",'8',True),
             Test("Nine",'9',True),
             Test("Letter", "a", False),
             Test("Letter 2", "t", False),
             Test("Capital", "M", False),
             Test("Capital 2", "Q", False),
             Test("Multi", '*',False),
             Test("Sub",'-',False)]

    fails = []
    for t in tests:
        result = io.isNumber(t.input)
        if t.output != result:
            fails.append(t)
            print("Test", t.name, "Fails Expected:", t.output, "Got:", result)
    print("isNumber Test Complete...")
    assert (len(fails) == 0)

def test_getPrecidence()->None:
    tests = [Test("Multi", '*',2),
             Test("Sub",'-',1),
             Test("Add",'+',1),
             Test("Div",'/',2),
             Test("Pow",'^',3),
             Test("No OP",' ', None)]

    fails = []
    for t in tests:
        result = io.getPrecedence(t.input)
        if t.output != result:
            fails.append(t)
            print("Test", t.name, "Fails Expected:", t.output, "Got:", result)
    print("isNumber Test Complete...")
    assert (len(fails) == 0)