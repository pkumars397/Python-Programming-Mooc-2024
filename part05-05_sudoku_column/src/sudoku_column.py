# Write your solution here
def column_correct(sudoku: list, column_no: int):
    num=[]
    for item in sudoku:
        if item[column_no]>0 and item[column_no] in num:
            return False;
        num.append(item[column_no])
        
    return True;