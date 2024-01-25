# Write your solution here
def fact(n:int):
    if n==1:
        return 1;
    return fact(n-1)*(n)

def factorials(n: int):
    dict={};
    for i in range(1,n+1):
        dict[i]=fact(i)
    return dict