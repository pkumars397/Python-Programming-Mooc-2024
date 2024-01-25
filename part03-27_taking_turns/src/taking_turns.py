# Write your solution here
num=int(input("enter limit: "))
i=1
j=num
while j>=num//2+1 and i<=num//2:
    print(i)
    print(j)
    i+=1
    j-=1
if num%2:
    print(num//2+1)