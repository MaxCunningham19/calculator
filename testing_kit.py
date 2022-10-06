from typing import List

class Test:
    def __init__(self, name: str, input, output) -> None:
        self.name = name
        self.input = input
        self.output = output


def runTests(tests: List[Test],function):
    fails = []
    for t in tests:
        result = test(t,function)
        if result != None:
            fails.append(result)
    return fails


def test(test:Test,function):
    fail = None
    result = function(test.input)
    if test.output != result:
        fail = test
        print("Test", test.name, "Fails Expected:", test.output, "Got:", result)
    return fail