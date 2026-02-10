#Operations.py--->File name and module name..
def sumop():
    print("Enter two values for addition:")
    a,b=float(input()),float(input())
    print("Sum ({},{})={}".format(a,b,a+b))
def subop():
    print("Enter two values for subtraction:")
    a, b = float(input()), float(input())
    print("Sub ({},{})={}".format(a, b, a - b))
def mulop():
    print("Enter two values for multiplication:")
    a, b = float(input()), float(input())
    print("Mul ({},{})={}".format(a, b, a * b))
def divop():
    print("Enter two values for Division:")
    a, b = float(input()), float(input())
    print("Division ({},{})={}".format(a, b, a / b))
    print("Floor Division ({},{})={}".format(a, b, a // b))
def modop():
    print("Enter two values for Mod Division:")
    a, b = float(input()), float(input())
    print("Mod Division ({},{})={}".format(a, b, a % b))
def expop():
    a, b = float(input("Enter base")), float(input("Enter power"))
    print("Power ({},{})={}".format(a, b, a ** b))