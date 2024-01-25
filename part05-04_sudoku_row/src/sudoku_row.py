# # Write your solution here
# def row_correct(sudoku: list, row_no: int):
#     contains=[1,2,3,4,5,6,7,8,9]
#     for item in sudoku[row_no]:
#         if  item!=0 and item not in contains:
#             return False
#         elif item!=0 and item in contains:
#             contains.remove(item)
#     return True;

def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)

    return True