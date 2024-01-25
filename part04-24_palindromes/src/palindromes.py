# Write your solution here
 
def palindromes(stri:str):
    revStr=""
    for i in range(len(stri)-1,-1,-1):
        revStr+=stri[i]
    if stri==revStr:
       return True
    else:
        return False
    
while True:
    userIn=input("please enter a string: ")
    if palindromes(userIn):
        print(f"{userIn} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

