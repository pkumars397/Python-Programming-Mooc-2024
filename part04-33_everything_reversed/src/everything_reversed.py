# Write your solution here
def everything_reversed(str_list:list)->list:
    str_list=str_list[::-1]
    for i in range(len(str_list)):
        str_list[i]=str_list[i][::-1]
    return str_list