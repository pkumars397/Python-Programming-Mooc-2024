# write your solution here
def largest():
    maxi=-1000000
    with open("./numbers.txt") as numbers_file:
        for (num) in numbers_file:
            num=int(num)
            if num>maxi:
                maxi=num
    
            
    return maxi

# largest()