# write your solution here
userInput=input("Please enter:")
a=[]
with open("./src/wordlist.txt") as input_file:
    for line in input_file:
        line=line.strip()
        a.append(line)
# print(a)
ans=''
userInput=userInput.split(" ")
# print(userInput)
for item in userInput:
    if item.lower() in a:
        ans+=item+" "
    else:
        newWord=f"*{item}* "
        ans+=newWord
print(ans)