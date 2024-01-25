# Write your solution here
def sum_of_positives(n:int):
    sum=0
    for i in n:
        if i>0:
            sum+=i
    return sum