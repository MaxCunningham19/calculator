from typing import List


class Test:
    def __init__(self, name: str, input, output) -> None:
        self.name = name
        self.input = input
        self.output = output


def runTests(tests: List[Test], function):
    fails = []
    for t in tests:
        result = test(t, function)
        if result is not None:
            fails.append(result)
    return fails


def test(t: Test, function):
    fail = None
    result = function(t.input)
    if t.output != result:
        fail = t
        print("Test", t.name, "Fails Expected:", t.output, "Got:", result)
    return fail
