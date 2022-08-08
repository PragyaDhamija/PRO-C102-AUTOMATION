import math
def add (x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y

print("Select Operation: \n 1) Addition \n 2) Subtraction \n 3) Multiplication \n 4) Division \n 5) Squaring \n 6) Square Root \n 7) Power a Number")
opt = input("\nEnter choice 1/2/3/4/5: ")

if opt == "1":
    number1 = int(input("\nEnter the first number: "))
    number2 = int(input("Enter the second number: "))
    print("\nSum is --> "+str(add(number1, number2)))
elif opt == "2":
    number1 = int(input("\nEnter the first number: "))
    number2 = int(input("Enter the second number: "))
    print("\nDifference is --> "+str(subtract(number1, number2)))
elif opt == "3":
    number1 = int(input("\nEnter the first number: "))
    number2 = int(input("Enter the second number: "))
    print("\nProduct is --> "+str(multiply(number1, number2)))
elif opt == "4":
    number1 = int(input("\nEnter the first number: "))
    number2 = int(input("Enter the second number: "))
    print("\nQuotient is --> "+str(divide(number1, number2)))
elif opt == "5":
    number = int(input("\nEnter the number: "))
    print("\nSquare is --> "+str(number*number))
elif opt == "6":
    number = int(input("\nEnter the number: "))
    print("\nSquare root is --> "+str(math.sqrt(number)))
elif opt == "7":
    number1 = int(input("\nEnter the number: "))
    number2 = int(input("Enter the power added to the number: "))
    print("\nSquare is --> "+str(number1**number2))
else:
    print("Invalid input")
    print("Please enter a number between 1 and 5...")