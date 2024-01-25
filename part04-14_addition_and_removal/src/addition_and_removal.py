# Write your solution here
list=[];
x=1;
i=0
while True:
    print("The list is now",list)
    userChoice=(input("add -> d ,remove -> r,exit -> x: "))
    if userChoice=="d":
        list.append(x)
        x+=1
    elif userChoice=="r":
        list.pop(len(list)-1)
        x-=1
    else:
        print("Bye!")
        break
    i+=1
    