# Write your solution here
def even_numbers(a:list):
    even_list=[]
    for i in a:
        if i%2==0:
            even_list.append(i)
    return even_list
# if __name__=="__main__":
#      even_numbers([1,2,3])