def calculator_num():

    number1 = int(input("First number: "))
    number2 = int(input("Second number: "))
    operation = input("Operation [+, -, *, /]: ")

    if operation == "/" and number2 == 0:
        combination = "you can't divide by zero."
    elif operation == "+":
        combination = number1 + number2
    elif operation == "-":
        combination = number1 - number2
    elif operation == "*":
        combination = number1 * number2
    elif operation == "/":
        combination = number1 / number2
    else:
        combination = "ERROR ... '" + operation + "not recognized."

    print(f"Answer: {combination}")


calculator_num()
