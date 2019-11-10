

# the main will be for concepts etc.

print("skipping to functions")


def my_function():
    print("this is a function")


def break_line():
    print("-------------------------------------------------------------------")


def arguments_function(first, second):
    break_line()
    print("this is the first one - " + first)
    print("this is the second - " + second)


def print_something(name, age):
    break_line()
    print("My name is", name, " and my age is", age)


def print_default(name="Someone", age="Unkown"):
    break_line()
    print("My name is", name, " and my age is", age)


my_function()
arguments_function("Number 1", "number 2")
arguments_function("A New number 1", "the best number 2")
print_something("Julio", 57)
print_default("Ronan")
print_default(age=66)


def print_people(*people):
    break_line()
    for person in people:
        print("This person is", person)


print_people("ronan", "Aoife", "Gizzy", "Peanut", "thierry", "Dennis", "Ian", "Emmanuel")