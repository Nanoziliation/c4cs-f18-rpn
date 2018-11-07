#!/usr/bin/env python3
import readline
from colorama import Fore, Back, Style

def calculate(arg):
    stack = []
    tokens = arg.split()
    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            elif token == '^':
                result = val1 ** val2

            stack.append(result)
    if len(stack) > 1:
        raise ValueError("Too many arguments on the stack")
    return stack[0]

    pass

def fun():
    print("fun")
    print("fun")
    print("fun")
    print("fun")
    print("fun")
    print("fun")
    print("fun")
    print("fun")
    print("fun")
    print("fun")
    print("fun")
    print("fun")

def main():
    while True:
        try:
            result = calculate(input("rpn clac> "))
            if (result > 0):
                print(Fore.GREEN + str(result) + Style.RESET_ALL)
            else:
                print(Fore.RED + str(result) + Style.RESET_ALL)
        except ValueError:
            pass

if __name__ == '__main__':
    main()
