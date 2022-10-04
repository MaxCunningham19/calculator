from input_organiser import calculate

if __name__ == "__main__":
    print("Welcome to simple calculator")
    running = True
    while running:
        stuff_to_calculate = input("Enter your calculation or quit: ")
        if stuff_to_calculate == "quit":
            running = False
        else:
            result = calculate(stuff_to_calculate)
            print(result)
    print("Program terminated")
