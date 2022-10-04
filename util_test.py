from testing_kit import Test
import util as util

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
        result = util.isNumber(t.input)
        if t.output != result:
            fails.append(t)
            print("Test", t.name, "Fails Expected:", t.output, "Got:", result)
    print("isNumber Test Complete...")
    assert (len(fails) == 0)

def test_isOperation()->None:
    tests = [Test("Zero",'0',False),
             Test("One", '1', False),
             Test("Two", '2', False),
             Test("Three", '3', False),
             Test("Four", '4', False),
             Test("Fives", '5', False),
             Test("Six",'6',False),
             Test("Seven",'7',False),
             Test("Eight",'8',False),
             Test("Nine",'9',False),
             Test("Letter", "a", False),
             Test("Letter 2", "t", False),
             Test("Capital", "M", False),
             Test("Capital 2", "Q", False),
             Test("Multi", '*',True),
             Test("Sub",'-',True),
             Test("Add","+",True),
             Test("Pow","^",True),
             Test("Div","/",True),
             Test("Modulo","%",False)]

    fails = []
    for t in tests:
        result = util.isOperation(t.input)
        if t.output != result:
            fails.append(t)
            print("Test", t.name, "Fails Expected:", t.output, "Got:", result)
    print("isNumber Test Complete...")
    assert (len(fails) == 0)