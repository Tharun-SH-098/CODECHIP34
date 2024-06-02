import math
print("General form:-ax**2+bx+c=0")
a=float(input("Enter a(a!=0):"))
b=float(input("enter b:"))
c=float(input("Enter c:"))
delta=(b**2)-4*a*c
if delta>0:
    x1=(((-b)+math.sqrt(delta))/(2*a))
    x2=(((-b)-math.sqrt(delta))/(2*a))
    print("There are two roots:%f and %f" %(x1,x2))
elif delta==0:
    x=(-b)/2*a
    print("There is one root",x)
else:
    print("Roots are imaginary,delta<0")
    
