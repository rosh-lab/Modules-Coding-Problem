#icici.py--->File name
bname="ICICI"
addr="HYD" #Here bname and addr are called global varaibles
def simpleint(): #Here this is called function definition
    p=float(input("Enter principal amount:"))
    t=float(input("Enter time:"))
    r=float(input("Enter rate of interest:"))
    #Cal si and total amt to pay.
    si=(p*t*r)/100
    tot=p+si
    print("-------------------------")
    print("Principal amount:{}".format(p))
    print("Time:{}".format(t))
    print("Rate of interest:{}".format(r))
    print("Simple interest:{}".format(si))
    print("Total amount:{}".format(tot))
    print("--------------------------------")
    
