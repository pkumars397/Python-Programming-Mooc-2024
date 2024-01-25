from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
x1=(-b+sqrt(b**2-4*a*c))/(2*a)
x2=(-b-sqrt(b**2-4*a*c))/(2*a)

print(f"The roots are {x1} and {x2}")