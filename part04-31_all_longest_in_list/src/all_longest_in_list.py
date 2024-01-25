# Write your solution here
def all_the_longest(arr:list):
    longest=0
    for item in arr:
        if len(item)>longest:
            longest=len(item)
    ans_longest=[]
    for i in range(len(arr)):
        if len(arr[i])==longest:
            ans_longest.append(arr[i])
    return ans_longest;