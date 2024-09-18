class Calculator():
    def __init__(self):
        self.operations = {
            '+': lambda x,y: x + y,
            '-': lambda x,y: x - y,
            '*': lambda x,y: x * y,
            '/': lambda x,y: x / y if y != 0 else "cannot be divided by 0"
        }
    
    def calculate(self,num1,operator,num2):
        return self.operations[operator](num1,num2)
        
calc = Calculator()
try:
    while True:
        num1 = float(input("enter first number: "))
        operator = input("enter operator (+, -, *, /): ")
        if operator in calc.operations:
            num2 = float(input("Enter the second number: "))
        else:
            print('Error: invalid operation')
            break
        print(f"Answer: {calc.calculate(num1, operator, num2)}")
        active = input("enter q to quit: ").lower()
        if active == "q":
            break
except ValueError:
    print("Error: only numeric values are allow. program closed")
except Exception:
    print("Error: Undefined. program closed")