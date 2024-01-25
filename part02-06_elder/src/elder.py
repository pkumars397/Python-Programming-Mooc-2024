# Write your solution here
# Write your solution here
name1=input("Person1: ")
age1=int(input("age: "))
name2=input("Person2: ")
age2=int(input("age: "))
if age1>age2:
    print(f"The elder is {name1}")
elif age2>age1 : print(f"The elder is {name2}")
else: print(f"{name1} and {name2} are the same age")