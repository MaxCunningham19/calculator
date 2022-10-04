from input_organiser import calculate
from validation import validateExpression

if __name__ == "__main__":
    print("Welcome to simple calculator")
    running = True
    while running:
        stuff_to_calculate = input("Enter your calculation or quit: ")
        if stuff_to_calculate == "quit":
            running = False
        else:
            isValid, index = validateExpression(stuff_to_calculate)
            if isValid:
                result = calculate(stuff_to_calculate)
                print(result)
            else:
                print("Invalid Input found at position",index)
    print("Program terminated")
