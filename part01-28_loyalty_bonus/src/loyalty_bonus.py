# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    total_points =points* 1.1
    print("Your bonus is 10 %")

if points >= 100:
    total_points=points* 1.15
    print("Your bonus is 15 %")

print("You now have", total_points, "points")