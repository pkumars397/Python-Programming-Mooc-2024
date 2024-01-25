# Write your solution here

dict={};
while True:
    
    userIn=input("choose a choice(1 search,2 insert,3 quit)")
    if userIn=="2":
         name=input("name: ")
         number=input("number: ")
         print("ok!")
         dict[name]=number
    elif userIn=="3":
        print("quitting...")
        break
    else:
        name=input("name: ")
        if name in dict:
            print(dict[name])
        else:
            print("no number")