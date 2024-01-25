# Write your solution here
list=[];
while True:
    nm=int(input("new number: "))
    if nm!=0:
        list.append(nm)
        print("The list now:",list)
        print("The list in order:",sorted(list))
    elif nm==0:
        print("Bye!")
        break;
    
