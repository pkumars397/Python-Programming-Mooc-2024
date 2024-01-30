# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

# student_info = "./src/students1.csv"
# exercise_data = "./src/exercises1.csv"

student_name={}
with open(student_info) as student_info_file:
    for line in student_info_file:
        # line=line.strip()
        parts=line.split(';')
        if parts[0]=="id":
            continue
        student_name[parts[0]]=parts[1]+" "+parts[2].strip()
# print(student_name)

exercises={}
with open(exercise_data) as exercise_file:
    for line in exercise_file:
        parts=line.split(';')
        if parts[0]=='id':
            continue
        else:
            grades=[int(parts[1]),int(parts[2]),int(parts[3]),int(parts[4]),int(parts[5]),int(parts[6]),int(parts[7])]
            exercises[parts[0]]=grades

for key in student_name:
    if key in exercises:
        totalexercise=sum(exercises[key])
        print(f"{student_name[key]} {totalexercise}")
    