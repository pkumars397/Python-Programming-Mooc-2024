# Write your solution here
def length(arr):
    count=0
    i=0
    while i<len(arr):
        count+=1
        i+=1
    return count
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)