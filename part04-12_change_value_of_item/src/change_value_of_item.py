list=[1, 2, 3, 4, 5]
while True:
    index=int(input("enter the index: "))
    if index!=-1:
        value=int(input("enter the value: "))
        list[index]=value
        print(list)
    else:
        break