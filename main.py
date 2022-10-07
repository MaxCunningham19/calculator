import util as util
import validation as valid
from evaluation import calculate


def processInput(stuff_to_calculate):
    if stuff_to_calculate == "quit":
        return False
    list_to_calculate = util.convertToList(stuff_to_calculate)
    validation_result = valid.validateExpression(list_to_calculate)
    if validation_result is not None:
        print(validation_result)
    else:
        result = calculate(stuff_to_calculate)
        print(result)
    return True


if __name__ == "__main__":
    print("Welcome to simple calculator")
    running = True
    while running:
        stuff_to_calculate = input("Enter your calculation or quit: ")
        running = processInput(stuff_to_calculate)
    print("Program terminated")
