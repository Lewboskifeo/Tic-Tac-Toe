theBoard = {'0': ' ', '1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' '}
notes = {'tl': '0', 'tm': '1', 'tr': '2', 'ml': '3', 'mm': '4', 'mr': '5', 'bl': '6', 'bm': '7', 'br': '8'}

def babyboard():
    print(theBoard["0"], "|", theBoard["1"], "|", theBoard["2"])
    print("---------")
    print(theBoard["3"], "|", theBoard["4"], "|", theBoard["5"])
    print("---------")
    print(theBoard["6"], "|", theBoard["7"], "|", theBoard["8"])
    
def pick():
    global T
    print(">> Enter your desired position on the board, ", TT, "'s turn: ", sep="")   
    T = input()
    return T
    
def win():
    global W, CW, L, p1, p3
    L = "X"
    for n in range(2):
        for i in range(3):
            if theBoard.get(str(p3), "") == L and theBoard.get(str(p3 + 1), "") == L and theBoard.get(str(p3 + 2), "") == L:
                W += 1
                break
            elif theBoard.get(str(0 + p1), "") == L and theBoard.get(str(3 + p1), "") == L and theBoard.get(str(6 + p1), "") == L:
                W += 1
                break
            elif theBoard.get(str(0), "") == L and theBoard.get(str(4), "") == L and theBoard.get(str(8), "") == L:
                W += 1
                break
            elif theBoard.get(str(6), "") == L and theBoard.get(str(4), "") == L and theBoard.get(str(2), "") == L:
                W += 1
                break
            p1 += 1
            p3 += 3
        p1 = 0    
        p3 = 0
        L = "O"
    return W

def loop():
    global TT, T, v, W, WW, fboard
    pick()
    fboard = notes.get(T, 0)
    for v in range(1):
        try:
            if theBoard[fboard] == "X":
                loop()
            elif theBoard[fboard] == "O":
                loop()
            else:
                break
        except:
            loop()
            break
    theBoard[fboard] = TT
    win()
    babyboard()
    if W >= 1:
        print(">> The player ", TT, " WON!!!", sep="")
        exit()
    if TT == "X":
        TT = "O"
    else:
        TT = "X"
    loop()

TT = "X"
T = ""
v = 0
W = 0
WW = ""
fboard = 0

p1 = 0
p3 = 0
CW = 0
L = ""
loop()
