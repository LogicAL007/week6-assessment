def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def division(x,y):
    if y==0:
        return "error"
    else:
        return x/y
def multiplication(x,y):
    return x * y



def calculator():
    prompt = input('what would like to do, add, sub, div, mult: ')
    x = int(input('enter the first num '))
    y = int(input('enter the second num '))
    output = 0
    if prompt == 'add':
        output = addition(x,y)
    elif prompt == 'sub':
        output = subtraction(x,y)
    elif prompt == 'div':
        output = division(x,y)
    elif prompt == 'mult':
        output= multiplication(x,y)
    else:
        print('invalid operation')
    return output


print(calculator())
