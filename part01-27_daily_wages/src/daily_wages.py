# Write your solution here
hourlyWage=float(input("Hourly wage:"))
hoursWorked=int(input("Hours worked:"))
weekDay=input("Day of the week:")
if(weekDay=="Sunday"):
    hourlyWage*=2;
total_wage=hourlyWage*hoursWorked;
print(f"Daily wages: {total_wage} euros");