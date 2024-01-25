# Write your solution here
# Write your solution here
count=0;
sum=0;
positive=0;
negative=0;
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num=int(input("type number: "))
    sum+=num
    count+=1
    if(num>0):
        positive+=1
    elif num<0:
        negative+=1
    else:
        count-=1
        break
mean=sum/(count)
print(f"Numbers typed in {count}\nThe sum of the numbers is {sum}\nThe mean of the numbers is {mean}\nPositive numbers {positive}\nNegative numbers {negative}")