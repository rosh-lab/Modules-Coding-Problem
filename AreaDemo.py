#AreaDemo.py-->File name.
from AreasMenu import AreasMenu
from AreaOperation import rectangle,triangle,square,circle
import sys
while True:
    AreasMenu()
    ch=input("Enter your choice:")
    match(ch):
        case "R"|"r":
            rectangle()
        case "T"|"t":
            triangle()
        case "S"|"s":
            square()
        case "C"|"c":
            circle()
        case "E"|"e":
            sys.exit()
        case _:
            print("Your selection of operations is wrong please try again")