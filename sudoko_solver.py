#Sudoko_solver written by Aimen BOULAHIA

#9x9 sudoku table
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
#Vizualisation function that helps to show us the table of sudoku
#indexes in python start from 0 (not 1)
def vizualise_board(b):
    for i in range(9):                             #length of the lines
        if i % 3 == 0:
                print("-----------------------------")
        for j in range(9):                      #length of each row
            if j % 3 == 0:                              #in case we are using another type of sudoku table we can replace 9 by len(b[0])
                print(" | ", end="")
            if j == 8:
                print(str(b[i][j]) + " | ")
            else:
                print(str(b[i][j]) + " ", end="")
    print("-----------------------------")
#vizualise_board(board)


def look_for_empty_case(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(b, value, position):

    #check column
    for i in range(9):
        if b[i][position[1]] == value and position[0] != i:  #check all the squares except the empty one
            return False
    #check row
    for i in range(9):
        if b[position[0]][i] == value and position[1] != i:  #check all the squares except the empty one
            return False
    #check intern-box
    box_j = position[1] // 3
    box_i = position[0] // 3

    for i in range(box_i*3, box_i*3 + 3):
        for j in range(box_j*3, box_j*3 + 3):
            if b[i][j] == value and (i,j) != position:
                return False
    return True
