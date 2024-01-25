# Write your solution here
def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(i):
            # temp=matrix[j][i]
            # matrix[j][i]=matrix[i][j]
            # matrix[i][j]=temp
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    


if __name__=="__main__":
    mat=[[1,2],[2,1]]
    transpose(mat)
    print(mat)