def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, //")
    
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /, //): ")
        num2 = float(input("Enter second number: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero")
                return
            result = num1 / num2
        elif operation == '//':
            if num2 == 0:
                print("Error: Division by zero")
                return
            result = num1 // num2
        else:
            print("Invalid operation")
            return
        
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers")

if __name__ == "__main__":
    calculator()