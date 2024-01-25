# Write your solution here
def line(num,string):
    if len(string)!=0:
        firstChar=string[0]
    else:
        firstChar="*"
    ans=""
    i=0
    while i<num:
         i+=1
         ans+=firstChar
    print(ans)
         
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "prashant")