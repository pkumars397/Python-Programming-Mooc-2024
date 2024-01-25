# Write your solution here
msg1=""
msg2=""
msg="";
while True:
    msg2=msg1
    msg1=input("Please type in a word: ")
    if(msg1=="end"):
        break
    elif msg1==msg2:
        break;
    msg+=msg1+" ";
print(msg)