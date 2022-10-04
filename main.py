from input_organiser import calculate

if __name__ == "__main__":
    print("Welcome to simple calculator")
    stuff_to_calculate = input("Enter your calculation: ")
    result = calculate(stuff_to_calculate)
    print(result)

