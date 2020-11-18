print("select a number for operation")
print("1 to add")
print("2 to subtract")
print("3 to multiply")
print("4 to divide")
print("5 to square")
print("6 for power")
print("7 for square root")
pass
operation = input()
pass
if operation == "1":
    num1 = input("enter a number")
    num2 = input("enter a number")
    print(str(int(num1) + int(num2)) + " is result")
    pass
if operation == "2":
    num1 = input("enter a number")
    num2 = input("enter a number")
    print(str(int(num1) - int(num2)) + " is result")
    pass
if operation == "3":
    num1 = input("enter a number")
    num2 = input("enter a number")
    print(str(int(num1) * int(num2)) + " is result")
    pass
if operation == "4":
    num1 = input("enter a number")
    num2 = input("enter a number")
    if num2 == "0":
        print(" Invalid value for denominator, can't divide by 0!")
    elif num2 != "0":
        print(str(int(num1) / int(num2)) + " is result")
        pass
    pass
if operation == "5":
    num1 = input("enter a number")
    print(str(int(num1) ** int(2)) + " is result")
    pass
if operation == "6":
    num1 = input("enter a number")
    num2 = input("to the power of")
    print(str(int(num1) ** int(num2)) + " is result")
    pass
if operation == "7":
    num1 = input("enter a number")
    print(str(float(num1) ** float(.5)) + " is result")
    pass