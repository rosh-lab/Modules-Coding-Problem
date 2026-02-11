#TempConversion.py--->File name and module name
def f_to_c():
    f=float(input("Enter temperature in Fahrenheit: "))
    c=(f-32)*5/9
    print("Farenheit to Celsius=",c)
def f_to_k():
    f=float(input("Enter temperature in Fahrenheit: "))
    k=(f-32)*5/9+273.15
    print("Farenheit to Kelvin=",k)
def c_to_f():
    c=float(input("Enter temperature in Celsius: "))
    f=(c*9/5)+32
    print("Celsius to Farenheit=",f)
def c_to_k():
    c=float(input("Enter temperature in Celsius: "))
    k=c+273.15
    print("Celsius to Kelvin=",k)
def k_to_f():
    k=float(input("Enter temperature in Kelvin: "))
    f=(k-273.15)*9/5+32
    print("Kelvin to Farenheit=",f)
def k_to_c():
    k=float(input("Enter temperature in kelvin: "))
    c=k-273.15
    print("Kelvin to Celsius=",c)
