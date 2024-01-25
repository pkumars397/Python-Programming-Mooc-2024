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

def box_of_hashes(height):
    # You should call function line here with proper parameters
    while height>0:
        height-=1
        line(10, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
