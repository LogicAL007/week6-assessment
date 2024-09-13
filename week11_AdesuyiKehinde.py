class BasicCalculator:
    def __init__(self):
        self.calculator()
    def calculator():
        print("Select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
                                                                  
    
        operation = input("Enter the number of the operation you want to perform (1/2/3/4): ")
    
        if operation in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except:
                print("Invalid input! Please enter numeric values.")
                return

        if operation == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} = {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} = {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} = {result}")
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} = {result}")
            else:
                print("Error! Division by zero is not allowed.")
        else:
            print("Invalid operation selection!")

    if __name__ == "__main__":
        calculator()
