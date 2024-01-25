# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
       for j in range(len(sudoku[0])):
            if (j)%3!=0:
              if sudoku[i][j]==0:
                print("_ ",end="")
              else:
                  print(f"{sudoku[i][j]} ",end="")
            else:
              if sudoku[i][j]==0:
                print(" _ ",end="")
              else:
                  print(f" {sudoku[i][j]} ",end="")
       print("\n")
            
def add_number(sudoku, row,col ,num ):
        sudoku[row][col]=num


if __name__=="__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)