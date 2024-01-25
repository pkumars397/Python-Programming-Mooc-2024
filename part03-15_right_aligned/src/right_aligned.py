# Write your solution here
# Write your solution here
userInput=input("Please type in a string: ")
if len(userInput)<20:
    print(f'{"*"*(20-len(userInput))}{userInput}')
else :
    print(userInput)