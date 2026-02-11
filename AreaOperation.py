#AreaOperation.py--->>File name and module name
def rectangle():
    l=float(input("Enter the length of the rectangle: "))
    b=float(input("Enter the breadth of the rectangle: "))
    arearec=l*b
    print("Area of rectangle=",arearec)
def triangle():
    b=float(input("Enter base:"))
    h=float(input("Enter height:"))
    areatri=0.5*b*h
    print("Area of triangle=",areatri)
def square():
    s=float(input("Enter side:"))
    areasq=s*s
    print("Area of square=",areasq)
def circle():
    r=float(input("Enter radius:"))
    areacir=3.14*r**2
    print("Area of circle=",areacir)