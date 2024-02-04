# wwite your solution here
import math
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data=input("Exam file:")

# student_info = "./src/students1.csv"
# exercise_data = "./src/exercises1.csv"
# exam_data=("./src/exam_points1.csv")
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
            total=int(parts[1])+int(parts[2])+int(parts[3])+int(parts[4])+int(parts[5])+int(parts[6])+int(parts[7])
            total=math.floor(total/40*100/10)
            exercises[parts[0]]=total
# print(exercises)
            
examsPoints={}
with open(exam_data) as exercise_file:
    for line in exercise_file:
        parts=line.split(';')
        if parts[0]=='id':
            continue
        else:
            grades=int(parts[1])+int(parts[2])+int(parts[3])
            examsPoints[parts[0]]=grades
# print(examsPoints)
gradePoints={}
for (key,val) in exercises.items():
    gradePoints[key]=exercises[key]+examsPoints[key]

# print(gradePoints)
for key,val in gradePoints.items():
    gradeawarded=0
    if val<15:
        gradePoints=0
    elif val>=15 and val<=17:
        gradeawarded=1
    elif val>=18 and val<=20:
        gradeawarded=2
    elif val>=21 and val<=23:
        gradeawarded=3
    elif val>=24 and val<=27:
        gradeawarded=4
    else:
        gradeawarded=5
    print(f"{student_name[key]} {gradeawarded}")