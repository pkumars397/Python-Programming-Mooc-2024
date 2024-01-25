# Write your solution here
noOfDaysWeek=int(input('how many days a week do you eat at the student cafeteria?'))
LunchPrice=float(input('the price of a typical student lunch?'))
groceryExp=float(input('How much money do you spend on groceries in a week?'))
dailyExp=(noOfDaysWeek/7)*LunchPrice+(groceryExp/7);
weeklyExp=LunchPrice*noOfDaysWeek+groceryExp;
print(f"Daily: {dailyExp} euros\nWeekly: {weeklyExp} euros")