# Write your solution here
def shortest(arr:list):
    shrt=len(arr[0])
    ans=arr[0]
    for item in arr:
        if len(item)<shrt:
            shrt=len(item)
            ans=item
    return ans;

if __name__=="__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"];
    print(shortest(my_list))