# Write your solution here
number1=int(input("Number 1:"))
number2=int(input("Number 2:"))
operator=input('Operation:')
if(operator=="add"):
    print(f'{number1} + {number2} = {number1+number2}');
if(operator=="subtract"):
    print(f'{number1} - {number2} = {number1-number2}');
if(operator=="multiply"):
    print(f'{number1} * {number2} = {number1*number2}');