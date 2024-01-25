# Write your solution here
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)

    return True

def column_correct(sudoku: list, column_no: int):
    num=[]
    for item in sudoku:
        if item[column_no]>0 and item[column_no] in num:
            return False;
        num.append(item[column_no])
        
    return True;

def block_correct(sudoku: list, row_no: int, column_no: int):
    num=[]
    for i in range(row_no,row_no+3):
        for j in range(column_no,column_no+3):
            if sudoku[i][j]>0 and sudoku[i][j] in num:
                return False;
            num.append(sudoku[i][j])
    return True;

def sudoku_grid_correct(sudoku: list):
    for row in range(len(sudoku)):
        if not row_correct(sudoku,row):
            return False;
    for col in range(len(sudoku[0])):
        if not column_correct(sudoku,col):
            return False;
    
    for row in range(0,len(sudoku)-2,3):
        for col in range(0,len(sudoku[0])-2,3):
            if not block_correct(sudoku,row,col):
                return False
    return True;

a=[1,2,4]
b=a
b[0]=20
print(id(a),id(b),a,b) #same reference both will change.