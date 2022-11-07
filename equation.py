#quadratic equation formula 
#a*x^2 + b*x + c = 0
import math
def calculateRoots(x,y,z):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Complex roots")
    elif delta == 0:
        print("Real and same roots")
        solution = ((-y)/2*x)
        print("Solution:", solution)
    else:
        deltaSquareRoot = math.sqrt(delta)
        print("Real and different roots")
        solution1 = (-y-deltaSquareRoot)/2*x
        solution2 = (-y+deltaSquareRoot)/2*x
        print("Solution 1:", solution1, "\n", "Solution2:", solution2)

print("Let's solve a quadratic equation.")
print("Using the following format, please enter your equation.")
print("a*x^2+b*x+c=0")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

if a!=0:
    calculateRoots(a,b,c)
else:
    if b!=0: #linear equation bx+c=0 -> x=-c/b
        print("The solution is" + str(-c/b))
    else: #a==0 && b==0, equation is c=0
        if c==0:
            print("Infinite solutions")
        else: 
            print("No existent solutions")
        