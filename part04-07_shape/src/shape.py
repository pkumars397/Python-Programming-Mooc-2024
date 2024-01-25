# Copy here code of line function from previous exercise and use it in your solution
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

def shape(size1,char1,size2,char2):
    i=1
    while i<=size1:
        line(i, char1)
        i+=1
    i=0
    while i<size2:
        line(size1,char2)
        i+=1
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x",3,"#")