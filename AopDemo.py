#AopDemo.py--->File name not module name because only statements are present here no global var and function name
from AopMenu import AopMenu
from Operations import sumop,subop,mulop,divop,modop,expop
import sys
while(True):
    AopMenu()
    ch=int(input("Enter your choice:"))
    match(ch):
        case 1:
            sumop()
        case 2:
            subop()
        case 3:
            mulop()
        case 4:
            divop()
        case 5:
            modop()
        case 6:
            expop
        case 7:
            sys.exit()
        case _:
            print("Your selection of operations is wrong---try again")
