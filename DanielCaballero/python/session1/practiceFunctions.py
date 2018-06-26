sum = "+"
subs = "-"
mult = "*"
div = "/"
mod = "%"
exp = "**"
floor = "//"

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def module(x, y):
    return x % y


def exponent(x, y):
    return x ** y


def floor_div(x, y):
    return x // y

def perform_operation(operator, number1, number2):
    if operator == sum:
        print(add(number1, number2))
    if operator == subs:
        print(subtract(number1, number2))
    if operator == mult:
        print(multiply(number1, number2))
    if operator == div:
        print(divide(number1, number2))
    if operator == mod:
        print(module(number1, number2))
    if operator == exp:
        print(exponent(number1, number2))
    if operator == floor:
        print(floor_div(number1, number2))

perform_operation("+",2,3)
perform_operation("-",20,10.52)
perform_operation("*",9,8.5)
perform_operation("/",25.0,5)
perform_operation("%",36,7)
perform_operation("**",3.0,4)
perform_operation("//",72,3)

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def module(x, y):
    return x % y


def exponent(x, y):
    return x ** y


def floor_div(x, y):
    return x // y
