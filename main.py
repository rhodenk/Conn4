# cols are numbered left to right, starting at 1
# row are numbers from the bottom, starting at 1

#colCount = 9
#rowCount = 9

gridData = "abcdefghiR......................................................................."


def indexsInCol(colNum):
    base = [1, 10, 19, 28, 37, 46, 55, 64, 73]
    return list(map(lambda x: x+(colNum-1), base))

def indexsInRow(rowNum):
    base = [1,2,3,4,5,6,7,8,9]
    return list(map(lambda x: x+(rowNum-1)*9, base))

def tokensInCol(colNum):
    tokens=""
    for i in indexsInCol(colNum):
        tokens += gridData[i-1]
    return tokens

def tokensInRow(rowNum):
    tokens=""
    for i in indexsInRow(rowNum):
        tokens += gridData[i-1]
    return tokens


def nextAvailableIndexInCol(colNum):
    c = tokensInCol(colNum)
    for i in range(0,9):
        if c[i] == ".":
            return i+1
    return -1 #i.e. full

def checkForWin():
    for c in 
    if "YYYY" in tokensInCol(1):
        return "Yellow WIN"
    if "RRRR" in tokensInCol(1):
        return "Red WIN"
    return ""


def addToken(colNum):
    global gridData
    n = nextAvailableIndexInCol(colNum)
    if n > 0:
        absIdx = ((n-1)*9)-1+colNum
        gridData = gridData[:absIdx] + "Y" + gridData[absIdx + 1:]
        return True
    else:
        return False  #col full, invalid move

#---------#---------#---------#---------#---------#---------#---------

def printGrid():
    for y in range(73, 0, -9):
        print(f"{(y+8)/9} - {gridData[y-1:y+8]}")

print("Start")
printGrid()
print("-----------------------")

for j in range(0, 12):
    print(f"Add token to 1 : {addToken(1)}")
    printGrid()
    print(checkForWin())
    print("-----------------------")
