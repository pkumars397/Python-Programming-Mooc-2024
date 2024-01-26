# Write your solution here
def older_people(people: list, year: int):
    newList=[];
    for item in people:
        if item[1]<year:
            newList.append(item[0])
    return newList;