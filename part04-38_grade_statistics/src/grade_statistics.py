# Write your solution here
def getDetails()->list:
    data=[]
    while True:
        user=input("please enter exam points and excercises completed: ")
        if not len(user):
            break;
        data.append(user.split())
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j]=int(data[i][j])
    return data;

examDetails=getDetails()

def pointsAvg(details:list)->float:
    sum=0
    for i in range(len(details)):
            sum+=details[i][0]+details[i][1]//10
    avg=sum/len(details)
    return avg;

def passing_percentage(details:list)->float:
    countOfPass=0
    for i in range(len(details)):
        if details[i][0]>=10:
           totalGrade=details[i][0]+details[i][1]//10
           if totalGrade>=15:
              countOfPass+=1
    
    return countOfPass/len(details)*100

def grade_wise_pass(arr:list)->list:
    passed_grade_wise=[];
    passed_grade_wise=[0]*6
    for i in range(len(arr)):
        if arr[i][0]>=10:
            totalGrade=arr[i][0]+arr[i][1]//10
            if totalGrade<15:
                  passed_grade_wise[0]+=1
            elif totalGrade>=15 and totalGrade<=17:
                  passed_grade_wise[1]+=1
            elif totalGrade>=18 and totalGrade<=20:
                  passed_grade_wise[2]+=1
            elif totalGrade>=21 and totalGrade<=23:
                  passed_grade_wise[3]+=1
            elif totalGrade>=24 and totalGrade<=27:
                  passed_grade_wise[4]+=1
            else:
                  passed_grade_wise[5]+=1
        else:
            passed_grade_wise[0]+=1;
    return passed_grade_wise;

avgpoint=f'{pointsAvg(examDetails):.1f}'
passPercent=f'{passing_percentage(examDetails):.1f}'
gradhist=grade_wise_pass(examDetails)
print("Statistics:")
print(f"Points average: {avgpoint}")
print("Pass percentage:",passPercent)
print("Grade distribution:")
print(f"5: {"*"*gradhist[5]}")
print(f"4: {"*"*gradhist[4]}")
print(f"3: {"*"*gradhist[3]}")
print(f"2: {"*"*gradhist[2]}")
print(f"1: {"*"*gradhist[1]}")
print(f"0: {"*"*gradhist[0]}")