# Write your solution here
# Write your solution here
str=input("Please type in a string: ")
char=input("Please tyep in substring: ")
index=str.find(char)
if index!=-1:
    str=str[index+len(char):]
    index2=str.find(char)
    if index2!=-1:
        print(f"The second occurrence of the substring is at index {index2+index+len(char)}.")
    else :
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")
