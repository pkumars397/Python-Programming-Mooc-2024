# Write your solution here
# Write your solution here
str=input("Word: ")
char=input("Char: ")
while True:
 index=str.find(char);
 if index!=-1 :
    slice3=str[index:index+3]
    if len(slice3)==3:
        print(slice3)
    str=str[index+1:]
 else:
     break