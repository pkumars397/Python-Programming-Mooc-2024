# Write your solution here
def oldest_person(people: list):
    max=people[0]
    for person in people:
        if person[1]<max[1]:
            max=person
    return max[0];

if __name__=="__main__":
    people_list = [('Arthur', 1977), ('Emily', 2014)]
    print(oldest_person(people_list))