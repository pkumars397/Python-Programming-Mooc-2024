# Write your solution here
while True:
    userInput=input("Please enter your editor: ")
    userInput=userInput.lower()
    if userInput=="vim" or userInput=="atom" or userInput=="emacs":
        print("not good")
    elif userInput=="notepad" or userInput=='word':
        print("awful")
    else:
        print("an excellent choice!")
        break