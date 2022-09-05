# Define the functions needed: add, sub, mul, div
from secrets import choice


def add(a, b):
    ans = a+b
    print(str(a)+" + "+str(b)+" = "+str(ans)+"\n")


def sub(a, b):
    ans = a-b
    print(str(a)+" - "+str(b)+" = "+str(ans)+"\n")


def mul(a, b):
    ans = a*b
    print(str(a)+" * "+str(b)+" = "+str(ans)+"\n")


def div(a, b):
    ans = a/b
    print(str(a)+" / "+str(b)+" = "+str(ans)+"\n")


while True:
    # print options to the user
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    # ask for values and call the functions
    choice = input("Enter your choice: ")
    choice = choice.upper()
    if choice == 'A':
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add(a, b)
    elif choice == 'B':
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub(a, b)
    elif choice == 'C':
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mul(a, b)
    elif choice == 'D':
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        div(a, b)
    elif choice == 'E':
        print("Program Ended")
        quit()
