import art
import os

# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Clear
def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print(art.logo)

    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    continue_calc = True

    while continue_calc:    
        operation_input = input('Pick an operation: ')
        num2 = float(input("What's the next number?: "))
        function = operations[operation_input]
        answer = function(num1, num2)

        print(f'{num1} {operation_input} {num2} = {answer}')
        keep_going = input(f'Type \'y\' to continue with {answer}, or type \'n\' to start a new calculation: ')

        if keep_going == 'y':
            num1 = answer
        else:
            continue_calc = False
            clear()
            calculator()

calculator()
            


