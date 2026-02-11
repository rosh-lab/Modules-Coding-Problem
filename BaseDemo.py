#BaseDemo.py--->File name
from BaseMenu import BaseMenu
from BaseConversion import d_to_b,d_to_o,d_to_h,b_to_d,b_to_o,b_to_h,o_to_d,o_to_b,o_to_h,h_to_d,h_to_b,h_to_o
import sys
while(True):
    BaseMenu()
    ch=int(input("Enter your choice:"))
    match(ch):
        case 1|2|3:
            d_to_b()
            d_to_o()
            d_to_h()
        case 4|5|6:
            b_to_d()
            b_to_o()
            b_to_h()
        case 7|8|9:
            o_to_d()
            o_to_b()
            o_to_h()
        case 10|11|12:
            h_to_d()
            h_to_b()
            h_to_o()
        case 13:
            sys.exit()
        case _:
            print("Invalid choice")