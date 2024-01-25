# Write your solution here
def mean(arr):
    total=sum(arr)
    length=len(arr)
    return total/length
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)