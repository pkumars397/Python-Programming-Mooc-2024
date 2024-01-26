# Write your solution here
def add_student(students:dict,name:str):
    students[name]={};

def print_student(students:dict,name:str):
    if name in students:
        length=len(students[name])
        print(name,":",sep="")
        if length==0:
            print(" no completed courses")
        else:
            grade=0
            print("",length,"completed courses: ")
            for key in students[name]:
                print(" ",key,students[name][key])
                grade+=students[name][key]
            avg=grade/length
            print(f" average grade {avg:.1f}");
    else:
        print(name ,": no such person in the database",sep="")

def add_course(students:dict,name:str,tup:tuple)->dict:
    courseDict=students[name];
    if tup[1]>0:
            if not tup[0] in courseDict:
                  courseDict[tup[0]]=tup[1]
            else:
                if courseDict[tup[0]]<tup[1]:
                    courseDict[tup[0]]=tup[1]
    
    
def summary(students):
    print("students",len(students))
    maxi={}
    name=""
    for key in students:
        if len(students[key])>len(maxi):
            maxi=students[key]
            name=key;
    print(f"most courses completed {len(maxi)} {name}")
    bestAvg=0
    stu=""
    for key in students:
         grade=0
         for key2 in students[key]:
                grade+=students[key][key2]
         avg=grade/len(students[key])
         if avg>bestAvg:
             bestAvg=avg
             stu=key
    print(f"best average grade {bestAvg} {stu}")
            
# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)