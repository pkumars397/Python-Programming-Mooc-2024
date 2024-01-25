# Write your solution here
num=int(input("number:"))
msg=''
if num%3==0 and num%5==0:
    msg+="FizzBuzz"
elif num%3==0:
    msg+="Fizz"
else: msg+="Buzz";
print(msg)