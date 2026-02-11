#BaseConversion.py---->>File name and module name
def d_to_b():
    n=int(input("Enter Decimal number:"))
    print("Binary=",bin(n)[2:])
def d_to_o():
    n=int(input("Enter Decimal number:"))
    print("Octal=",oct(n)[2:])
def d_to_h():
    n=int(input("Enter Decimal number:"))
    print("Hexadecimal=",hex(n)[2:])
def b_to_d():
    n=input("Enter Binary number:")
    print("Decimal=",int(n,2))
def b_to_o():
    n=input("Enter Binary number:")
    print("Octal=",oct(int(n,2))[2:])
def b_to_h():
    n=input("Enter Binary number:")
    print("Hexadecimal=",hex(int(n,2))[2:])
def o_to_d():
    n=input("Enter Octal number:")
    print("Decimal=",int(n,8))
def o_to_b():
    n=input("Enter Octal number:")
    print("Binary=",bin(int(n,8))[2:])
def o_to_h():
    n=input("Enter Octal number:")
    print("Hexadecimal=",hex(int(n,8))[2:])
def h_to_d():
    n=input("Enter Hexadecimal number:")
    print("Decimal=",int(n,16))
def h_to_b():
    n=input("Enter Hexadecimal number:")
    print("Binary=",bin(int(n,16))[2:])
def h_to_o():
    n=input("Enter Hexadecimal number:")
    print("Octal=",oct(int(n,16))[2:])