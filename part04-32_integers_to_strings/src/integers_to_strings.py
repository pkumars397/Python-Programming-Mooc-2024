# Write your solution here
def formatted(arr:list):
    string_list=[]
    for item in arr:
        string_list.append(f"{item:.2f}")
    return string_list;