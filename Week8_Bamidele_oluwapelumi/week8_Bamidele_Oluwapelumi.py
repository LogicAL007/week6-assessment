operations = {
    "1":{"name":"addition", "function": lambda x,y: x + y},
    "2":{"name":"subtraction", "function": lambda x,y: x - y},
    "3":{"name":"multiplication", "function": lambda x,y: x * y},
    "4":{"name": "division", "function": lambda x,y: x / y if y != 0 else "cannot be divided by 0"}
    }

def calculator():
    print("operation:")
    for key, value in operations.items():
        print(f"{key}-->{value['name']}")

    choice = input("enter the operation you want to perform(1-4): ")

    if choice in operations:
        num_1 = float(input("enter the first number: "))
        num_2 = float(input("enter the second number: "))
        calc = operations[choice]['function'](num_1,num_2)
        print("Answer:", calc)
    else:
        print("invalid!")

try:
    while True:
        calculator()
        active = input("enter q to quit: ").lower()
        if active == "q":
            break
except ValueError:
    print("Error: only numeric values are allow")
except Exception:
    print("Error: Undefined")
    