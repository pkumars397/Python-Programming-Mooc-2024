# write your solution here
def mat_format():
    new_mat=[]
    with open("./src/matrix.txt") as matrix_file:
        for row in matrix_file:
            row=row.replace("\n",'')
            row=row.split(" ")
            for item in row:
                item=item.split(",")
                j=[]
                for i in item:
                    j.append(int(i))
                new_mat.append(j)
    return new_mat

def matrix_sum():
   result= mat_format()
   total=0
   for row in result:
       total+=sum(row)
       
   return total

def matrix_max():
    result=mat_format()
    maxi=-10**18
    for row in result:
        maxInRow=max(row)
        if maxInRow>maxi:
            maxi=maxInRow
    # print(maxi)
    return maxi

def row_sums():
    result=mat_format()
    ans_list=[]
    for row in result:
        total=sum(row)
        ans_list.append(total)
    # print(ans_list)
    return ans_list

