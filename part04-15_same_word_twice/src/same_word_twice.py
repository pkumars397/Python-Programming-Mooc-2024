# Write your solution here
list=[]
count=0
while True:
    take=input("please enter: ")
    if len(list)==0:
        list.append(take)
    else: 
        if take in list:
            break
        else:
            list.append(take)
print("You typed in",len(list),"different words")