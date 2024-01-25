# Write your solution here
while True:
    num=int(input("Please type in a number: "))
    if num>0:
       i=1
       fact=1
       while i<=num:
        fact*=i
        i+=1
    else:
        print("Thanks and bye!")
        break
    print("The factorial of the number",num,"is",fact)