# Write your solution here
grade=int(input("How many points [0-100]: "))
msg="";
if grade<0:
    msg+="impossible!"
elif grade>=0 and grade<=49:
    msg+="fail"
elif grade>=50 and grade<=59:
    msg+="1"
elif grade>=60 and grade<=69:
    msg+="2"
elif grade>=70 and grade<=79:
    msg+="3"
elif grade>=80 and grade<=89:
    msg+="4"
elif grade>=90 and grade<=100:
    msg+="5"
else: msg+="impossible!"
print(f"Grade: {msg}")