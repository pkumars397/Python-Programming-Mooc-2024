# Write your solution here
password=input("Password:")
while True:
    repeatPass=input("Repeat Password:")
    if(password==repeatPass):
        print("User account created!")
        break;
    else:
        print("They do not match!")