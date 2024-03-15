from art import logo
from os import system

def add(num1,num2):
    """Adds two numbers and returns their sum"""
    return num1 + num2

def subtract(num1,num2):
    """Subtracts two numbers and returns their difference"""
    return num1 - num2

def multiply(num1,num2):
    """Multiplies two numbers and returns their product"""
    return num1 * num2

def divide(num1,num2):
    """Divides two numbers and returns their quotient"""
    return num1 / num2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operator = input("Pick an operation : ")
        num2 = float(input("What is the next number?: "))
        if operator in operations:
            answer = operations[operator](num1,num2)

        print(f"{num1} {operator} {num2} = {answer}")
        new_number = input(f"Type 'y' to continue calculating with {answer},type 'n' to start again: ").lower
        if new_number == "y":
            num1 = answer
        else:
            should_continue = False
            system("clear")
            calculator()

calculator()