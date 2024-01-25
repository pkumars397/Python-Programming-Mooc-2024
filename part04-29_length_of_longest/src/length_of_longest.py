# Write your solution here
def length_of_longest(str_list:list):
    best=0
    for item in str_list:
        if len(item) > best:
            best=len(item)
    return best
            
        