import re

print("My great calculator")
print("Type quit to exit")

previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter Equation")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye Nerd")
        run = False
    else:
        equation = re.sub('[a-zA-z,.():" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
            print(eval(equation))
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()
