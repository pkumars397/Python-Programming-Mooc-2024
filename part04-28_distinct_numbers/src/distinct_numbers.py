# Write your solution here
# def distinct_numbers(a:list):
#     distinct_num=[]
#     a.sort()
#     for i in range(len(a)-1):
#         if a[i]!=a[i+1]:
#             distinct_num.append(a[i])
#     distinct_num.append(a[len(a)-1])
#     return distinct_num
def distinct_numbers(my_list: list):
    results = []
    for item in my_list:
        if item not in results:
            results.append(item)

    results.sort()
    return results