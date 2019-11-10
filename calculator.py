import re

print("My great calculator")
print("Type quit to exit")

previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = input("Enter Equation")
    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-z,.():" "]', '', equation)
        previous = eval(equation)
        print("You typed", equation)
        print("The answer is", eval(equation))


while run:
    perform_math()


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


