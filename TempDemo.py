#TempDemo.py--->File name...
from TempMenu import TempMenu
from TempConversion import f_to_c,f_to_k,c_to_f,c_to_k,k_to_f,k_to_c
import sys
while True:
    TempMenu()
    ch=int(input("Enter your choice:"))
    match(ch):
        case 1:
            f_to_c()
        case 2:
            f_to_k()
        case 3:
            c_to_f()
        case 4:
            c_to_k()
        case 5:
            k_to_f()
        case 6:
            k_to_c()
        case 7:
            sys.exit()
        case _:
            print("Your selection was not recognised..try again")
