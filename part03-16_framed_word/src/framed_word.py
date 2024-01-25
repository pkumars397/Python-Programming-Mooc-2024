# Write your solution here
# Write your solution here
str=input("Word: ")
frame="*"*30
print(frame)
spaces=30-len(str)-2
if spaces%2:
    middle="*"+" "*((spaces)//2)+str+" "*((spaces)//2+1)+"*"
else :
    middle="*"+" "*((spaces)//2)+str+" "*((spaces)//2)+"*"
print(middle)
print(frame)