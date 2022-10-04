import input_organiser as io
from testing_kit import Test


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