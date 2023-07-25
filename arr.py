import os

# app config
ROW_COUNT = 6
COL_COUNT = 9
WIN_COUNT = 4

grid = [["."] * COL_COUNT for i in range(ROW_COUNT)]  #create grid "array" with nested lists.  Grid dimensions are rows then cols : grid(r, c)
    
def getCol(col):
    tokens = ""
    for i in range(0,ROW_COUNT):
        tokens += grid[i][col]
    return tokens

def getRow(row):
    tokens = ""
    for i in range(0,COL_COUNT):
        tokens += grid[row][i]
    return tokens

def getFDiagonal(diag):
    tokens = ""
    if diag < ROW_COUNT:   #diagonal numbering is artificial, so separate between row and col count
        for r in range(diag,diag+1):
            for c in range(0,COL_COUNT):
                if r-c < 0:
                    break
                tokens += grid[r-c][c]
        #print(f"fDiag{diag} >> {tokens}")
    else:
        for c in range(diag-ROW_COUNT, diag-ROW_COUNT+1):    #start at 1 - skip first as this was already included above for c in range(1, COL_COUNT):
            for r in range(0,ROW_COUNT):
                if r+c >= COL_COUNT-1:
                    break
                #print(f"{r} {c} >> {ROW_COUNT-r-1},{r+c+1}")
                tokens += grid[ROW_COUNT-r-1][r+c+1]
        #print(f"fDiag{diag} >> {tokens}")
    return tokens

def getBDiagonal(diag):
    tokens = ""
    if diag < ROW_COUNT:   #diagonal numbering is artificial, so separate between row and col count
        for r in range(diag,diag+1):        # 0..0
            for c in range(0,COL_COUNT):    # 0..8
                if c+r > ROW_COUNT-1:
                    break
                tokens += grid[c+r][c]
                #print(f"{c+r},{c} = {grid[c+r][c]}")
    else:
        for c in range(diag-ROW_COUNT+1, diag-ROW_COUNT+2):    #start at +1 - skip first as this was already included above
            for r in range(0,ROW_COUNT):
                if r+c >= COL_COUNT:
                    break
                tokens += grid[r][r+c]
                #print(f"{r} {c} >> {r},{r+c} = {grid[r][r+c]}")
    #print(f"bDiag{diag} >> {tokens}")
    return tokens

def addToken(col, player):
    i = 0
    for t in getCol(col):
        if t==".":
            grid[i][col] = player
            return True
        i+=1
    return False   #col full

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
    for i in range(0, COL_COUNT):
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

clearScreen()
print(f"Start - get {WIN_COUNT} in a row to win")
printGrid()

userCol = ""
whoseGo = "R"
allowedInputs = []
for i in range(0, COL_COUNT):
    allowedInputs.append(str(i))

while userCol!="X":
    userCol = input(f"Player {whoseGo}, enter column number from 0 to {COL_COUNT-1}: ")
    clearScreen()
    if userCol in allowedInputs:        #make dynamic
        if addToken(int(userCol), whoseGo):
            printGrid()
            #print(getFDiagonal(int(userCol)))
            w = checkWin()
            if w!="":
               print(f"win={w}")
               userCol = "X"
            whoseGo="Y" if whoseGo=="R" else "R"
        else:
            print("Column is full.  Choose a different column")
            printGrid()
    else:
        print("bad input")
        printGrid()