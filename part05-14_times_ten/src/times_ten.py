# Write your solution here
def times_ten(start_index: int, end_index: int):
    dict={};
    for i in range(start_index,end_index+1):
        dict[i]=10*i
        
    return dict