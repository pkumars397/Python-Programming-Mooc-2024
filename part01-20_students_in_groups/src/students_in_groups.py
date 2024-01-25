# Write your solution here
students=int(input('How many students on the course?'))
group_size=int(input('Desired group size?'))
numberOfGroups=(students//group_size)
numberOfGroups=numberOfGroups+1 if students%group_size!=0 else numberOfGroups
print(f"Number of groups formed: {numberOfGroups}")