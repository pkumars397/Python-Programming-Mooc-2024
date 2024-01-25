# Copy here code of line function from previous exercise
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
    
def square_of_hashes(size):
    # You should call function line here with proper parameters
    i=0
    while i<size:
        i+=1
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(3)
