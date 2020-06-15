class cell(object):
    def __init__(self):
        self.col = 0
        self.row = 0
        self.square = 0
        self.contains = "_"
        self.possible = []
squareArray = [[10 for x in range(9)] for y in range(9)]
for x in range(9):
    squareArray[x].clear()
def lazy_square_setter():
    for y in reversed(range(9)):
        for x in range(9):
            if x<3 and y<3:
                squareArray[0].append(board[x][y])
                board[x][y].square=0
            if 2<x<6 and y<3:
                squareArray[1].append(board[x][y])
                board[x][y].square=1
            if x>5 and y<3:
                squareArray[2].append(board[x][y])
                board[x][y].square=2
            if x<3 and 2<y<6:
                squareArray[3].append(board[x][y])
                board[x][y].square=3
            if 2<x<6 and 2<y<6:
                squareArray[4].append(board[x][y])
                board[x][y].square=4
            if x>5 and 2<y<6:
                squareArray[5].append(board[x][y]) 
                board[x][y].square=5
            if x<3 and y>5:
                squareArray[6].append(board[x][y])
                board[x][y].square=6
            if 2<x<6 and y>5:
                squareArray[7].append(board[x][y])
                board[x][y].square=7
            if x>5 and y>5:
                squareArray[8].append(board[x][y])
                board[x][y].square=8

def row_and_col_setter():
    for z in range(9):
        for x in range (9):
            board[x][z].col = x
            board[z][x].row = x
            

def display_board():
    for y in reversed(range(9)):
        if y == 2 or y == 5 or y ==8:
            print("\n")
        else:
            print("")
        for x in range(9):
            if x == 2 or x == 5 or x==8:
                print(board[x][y].contains, end="   ")
            elif x == 0:
                print("  ", end="")
                print(board[x][y].contains, end="|")
            else:
                print(board[x][y].contains, end="|")
    print("")

def set_easy_board():
    board[3][0].contains = 1
    board[6][0].contains = 8
    
    board[2][1].contains = 6
    board[7][1].contains = 2
    board[8][1].contains = 4
    
    board[0][2].contains = 4
    board[2][2].contains = 8
    board[3][2].contains = 6
    board[5][2].contains = 3
    board[7][2].contains = 7
    board[8][2].contains = 1
    
    board[2][3].contains = 3
    board[3][3].contains = 4
    board[4][3].contains = 2
    board[5][3].contains = 6
    board[8][3].contains = 8
    
    board[3][4].contains = 9
    board[5][4].contains = 8
    
    board[0][5].contains = 8
    board[3][5].contains = 5
    board[4][5].contains = 1
    board[5][5].contains = 7
    board[6][5].contains = 6
    
    board[0][6].contains = 6
    board[1][6].contains = 3
    board[3][6].contains = 8
    board[5][6].contains = 5
    board[6][6].contains = 7
    board[8][6].contains = 2
    
    board[0][7].contains = 2
    board[1][7].contains = 9
    board[6][7].contains = 4
    
    board[2][8].contains = 7
    board[5][8].contains = 4
    
numsall = [1,2,3,4,5,6,7,8,9]
counter=0
takennums = []
def solved_cells(dataneeds):
    if (dataneeds != 0):
        print("viable solutions for missing numbers generated.")
    counter=0
    for x in range(9):
        for y in range(9):
            for square in squareArray[board[x][y].square]:
                takennums.append(square.contains)
            for sweep in range(9):
                if board[x][sweep].contains != '_':
                    takennums.append(board[x][sweep].contains)
                if board[sweep][y].contains != '_':
                    takennums.append(board[sweep][y].contains)
            for z in range(len(numsall)):
                if numsall[z] not in takennums:
                    board[x][y].possible.append(numsall[z])
            if (len(board[x][y].possible) == 1) and (board[x][y].contains == '_'):
                counter+=1
                board[x][y].contains = board[x][y].possible[0]
            else:
                if (dataneeds==0):
                    board[x][y].possible.clear()
            takennums.clear()
    if counter!=0:
        solved_cells(0)
hidden_singles_array = []

def hidden_singles():
    solved_cells(1)
    z=0
    for x in range(9):
        for y in range(9):
            hidden_singles_array.clear()
            for square in squareArray[(board[x][y].square)]:
                if (square.contains == '_'):
                    hidden_singles_array.extend(square.possible)
            hidden_singles_array.sort()
            for z in range((len(numsall))): 
                if (hidden_singles_array.count(numsall[z])  == 1):
                    for square in squareArray[(board[x][y].square)]:
                        if (numsall[z] in square.possible and square.contains == '_'):
                            square.contains = numsall[z]
        solved_cells(0)


board = [[cell() for x in range(9)] for y in range(9)]
lazy_square_setter()
row_and_col_setter()
set_easy_board()
display_board()
solved_cells(0)
print("solved cells done")
hidden_singles()
print("hidden singles done")
display_board()
