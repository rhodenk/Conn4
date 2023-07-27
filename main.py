import os

# app config
ROW_COUNT = 6
COL_COUNT = 9
WIN_COUNT = 4

grid = [["."] * COL_COUNT for i in range(ROW_COUNT)]  #create grid "array" with nested lists.  Grid dimensions are rows then cols : grid(r, c)
    
def getCol(col):        # return string of tokens in column with index 'col'
    tokens = ""
    for i in range(0,ROW_COUNT):
        tokens += grid[i][col]
    return tokens

def getRow(row):        # return string of tokens in row with index 'row'
    tokens = ""
    for i in range(0,COL_COUNT):
        tokens += grid[row][i]
    return tokens

def getFDiagonal(diag):     # return string of tokens in fdiagonal with index 'diag'
    tokens = ""
    if diag < ROW_COUNT:   #diagonal numbering is artificial, so separate between row and col count
        for c in range(0,COL_COUNT):
            if diag-c < 0:     #  allow for edge diagonals with less items
                break
            tokens += grid[diag-c][c]
    else:
        c = diag-ROW_COUNT
        for r in range(0,ROW_COUNT):
            if r+c >= COL_COUNT-1:
                break
            tokens += grid[ROW_COUNT-r-1][r+c+1]
    return tokens

def getBDiagonal(diag):          # return string of tokens in bdiagonal with index 'diag'
    tokens = ""
    if diag < ROW_COUNT:   #diagonal numbering is artificial, so separate between row and col count
        for c in range(0,COL_COUNT):
            if c+diag > ROW_COUNT-1:
                break
            tokens += grid[c+diag][c]
    else:
        c = diag-ROW_COUNT+1
        for r in range(0,ROW_COUNT):
            if r+c >= COL_COUNT:
                break
            tokens += grid[r][r+c]
    return tokens

def addToken(col, player):
    i = 0
    for t in getCol(col):       #work upwards until a "." is found
        if t==".":
            grid[i][col] = player
            return True
        i+=1
    return False   #default - no "." found so column is full

def checkStringForWin(checkString):
    if "Y"*WIN_COUNT in checkString:
        return "Y"
    if "R"*WIN_COUNT in checkString:
        return "R"
    return ""

def checkWin():
    checkString = ""
    for i in range(ROW_COUNT):
        checkString = checkStringForWin(getRow(i))
        if checkString != "":
            return checkString
    for i in range(COL_COUNT):
        checkString = checkStringForWin(getCol(i))
        if checkString != "":
            return checkString
    for i in range(ROW_COUNT+COL_COUNT-1):
        checkString = checkStringForWin(getFDiagonal(i))
        if checkString != "":
            return checkString
    for i in range(ROW_COUNT+COL_COUNT-1):
        checkString = checkStringForWin(getBDiagonal(i))
        if checkString != "":
            return checkString
    return ""   # default - no win this time

#------------------------------------------------------------------------------------------------------------------------

def printHeader():
    for i in range(1, COL_COUNT+1):
        print(f"\x1b[0;34;40m {i}\x1b[0m", end="")
    print("\x1b[0;34;40m \x1b[0m")  #newline

def printGrid():
    printHeader()
    colourMapper = {"R": "\x1b[0;31;40m ●\x1b[0m","Y": "\x1b[0;33;40m ●\x1b[0m"}   
    for r in range(ROW_COUNT-1, -1, -1):                #go in -1 direction because people like to think of row 1 as the "bottom", because gravity
        row = ""
        for c in range(0, COL_COUNT):
            row += colourMapper.get(grid[r][c], "\x1b[0;37;40m ○\x1b[0m")
        row += "\x1b[0;37;40m \x1b[0m"
        print(row)

def clearScreen():
    if os.name == 'nt':     # for windows numptys not using WSL
        _ = system('cls')
    else:
        _ = os.system('clear')


if __name__ == '__main__':      # don't include UI in unit tests
    clearScreen()
    print(f"Start - get {WIN_COUNT} in a row to win.  Enter 'X' to exit")
    printGrid()

    userCol = ""
    whoseGo = "R"
    allowedInputs = []
    for i in range(1, COL_COUNT+1):
        allowedInputs.append(str(i))

    while userCol!="X":
        userCol = input(f"Player {whoseGo}, enter column number from 1 to {COL_COUNT}: ")
        clearScreen()
        if userCol in allowedInputs:        #make dynamic
            if addToken(int(userCol)-1, whoseGo):
                printGrid()
                w = checkWin()
                if w!="":
                    print(f"{w} wins!")
                    userCol = "X"
                whoseGo="Y" if whoseGo=="R" else "R"
            else:
                printGrid()
                print("\x1b[0;31;40mColumn is full.  Choose a different column\x1b[0m ")
        else:
            printGrid()
            print("\x1b[0;31;40mInvalid input\x1b[0m ")