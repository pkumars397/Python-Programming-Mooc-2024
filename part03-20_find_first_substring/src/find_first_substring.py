# Write your solution here
# Write your solution here
str=input("string: ")
char=input("Please enter char: ")
index=str.find(char)
if str.find(char)>=0:
    sliced=str[index:index+3]
    if len(sliced)==3:
        print(sliced)