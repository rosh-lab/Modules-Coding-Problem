#SharesDemo.py--Viewer program
import Shares,time,importlib
def dispshares(d):
    print("*"*50)
    print("\t\tShareName\t\tShareValue")
    for sn,sv in d.items():
        print("\t\t{} \t\t\t\t{}".format(sn,sv))

#Main program......
d=Shares.sharesinfo()
dispshares(d)
print("I am going to sleep for 15 seconds")
time.sleep(15)
print("I am coming out off sleep after 15 seconds")
importlib.reload(Shares)
d=Shares.sharesinfo()
dispshares(d)
print("I am going to sleep for 20 seconds")
time.sleep(20)
print("I am coming out off sleep after 20 seconds")
importlib.reload(Shares)
d=Shares.sharesinfo()
dispshares(d)