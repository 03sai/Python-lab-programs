import math
import cmath
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
disc=b**2-4*a*c

if disc<0:
    print("Imaginary roots")
    realp=float(-b/2*a)
    imagp=cmath.sqrt(abs(disc))/(2.0*a)
    print("realp:",realp)
    print("imagp:",imagp)

elif disc==0:
    print("Roots are real and equal")
    root1=float(-b/2*a)
    root2=root1
    print("root1:",root1)
    print("root2:",root2)

elif disc>0:
    print("Roots are real and distinct")
    root1=(-b+cmath.sqrt(disc))/(2*a)
    root2=(-b-cmath.sqrt(disc))/(2*a)
    print("root1:",root1)
    print("root2:",root2)     
