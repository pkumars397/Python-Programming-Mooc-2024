from math import sqrt
# Write your solution here
from math import sqrt
# Write your solution here
while True:
    num=int(input("Please type in a number: "))
    if num==0:
        print("Exiting...")
        break;
    elif num>0:
        print(sqrt(num));
    else:
        print("Invalid number")