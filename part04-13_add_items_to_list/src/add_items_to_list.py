# Write your solution here
list=[];
limit=int(input("enter the number of items u want to add to the list: "));
while limit>0:
    number=int(input("enter num to insert: "))
    list.append(number)
    limit-=1
    
print(list)