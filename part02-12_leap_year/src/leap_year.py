# Write your solution here
year=int(input("please enter year:"))
msg="";
if year%4==0:
    if year%100==0:
        if year%400==0:
           msg+="That year is a leap year."
        else:
            msg+="That year is not a leap year."
    else:
        msg+="That year is a leap year."
else:
    msg+="That year is not a leap year."
print(msg)