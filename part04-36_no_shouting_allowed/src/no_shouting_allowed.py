# Write your solution here
def no_shouting(arr:list)->list:
    newList=[]
    for item in arr:
        if not item.isupper():
            newList.append(item)
    return newList;