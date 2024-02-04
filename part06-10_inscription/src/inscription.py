# Write your solution here
inp=input("Whom should I sign this to:")
fileName=input("Where shall I save it:")
with open(fileName,"w") as fileName:
    fileName.write(f"Hi {inp}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")