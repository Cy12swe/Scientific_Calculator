import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def square_root(x):
    if x < 0:
        return "Invalid input for square root"
    return math.sqrt(x)

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Invalid input for logarithm"
    return math.log(x, base)

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'sqrt' for square root")
    print("Enter 'log' for logarithm")
    print("Enter 'sin' for sine")
    print("Enter 'cos' for cosine")
    print("Enter 'tan' for tangent")
    print("Enter 'pi' to use π")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ["add", "subtract", "multiply", "divide"]:
        num1 = input("Enter first number: ")
        if num1 == 'pi':
            num1 = math.pi
        else:
            num1 = float(num1)

        num2 = input("Enter second number: ")

        if num2 == 'pi':
            num2 = math.pi
        else:
            num2 = float(num2)
        
        if user_input == "add":
            print("Result: ", add(num1, num2))
        elif user_input == "subtract":
            print("Result: ", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result: ", multiply(num1, num2))
        elif user_input == "divide":
            print("Result: ", divide(num1, num2))
    elif user_input == "sqrt":
        num = input("Enter a number: ")
        if num == 'pi':
            num = math.pi
        else:
            num = float(num)
        print("Result: ", square_root(num))
    elif user_input == "log":
        num = input("Enter the number: ")
        if num == 'pi':
            num = math.pi
        else:
            num = float(num)
        base = float(input("Enter the base: "))
        print("Result: ", logarithm(num, base))
    elif user_input in ["sin", "cos", "tan"]:
        angle = input("Enter an angle in degrees: ")
        if angle == 'pi':
            angle = math.pi
        else:
            angle = float(angle)
        if user_input == "sin":
            print("Result: ", math.sin(math.radians(angle)))
        elif user_input == "cos":
            print("Result: ", math.cos(math.radians(angle)))
        elif user_input == "tan":
            print("Result: ", math.tan(math.radians(angle)))
    elif user_input == "pi":
        print("π (pi) =", math.pi)
    else:
        try:
            result = eval(user_input)
            print("Result: ", result)
        except Exception as e:
            print("Invalid input:", str(e))
