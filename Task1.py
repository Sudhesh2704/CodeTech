# Basic Calculator Program

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    print("Welcome to the Basic Calculator!")
    
    # Getting user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Displaying operation choices
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("\nEnter the number corresponding to the operation (1/2/3/4): ")

    # Performing the chosen operation
    if operation == '1':
        result = add(num1, num2)
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid operation. Please choose between 1, 2, 3, or 4.")

# Running the calculator
calculator()
