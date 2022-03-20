import sys

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
    global W, L, P1, P3
    L = "X"
    for n in range(2):
        for i in range(3):
            if theBoard.get(str(P3), "") == L and theBoard.get(str(P3 + 1), "") == L and theBoard.get(str(P3 + 2), "") == L:
                W += 1
                break
            elif theBoard.get(str(0 + P1), "") == L and theBoard.get(str(3 + P1), "") == L and theBoard.get(str(6 + P1), "") == L:
                W += 1
                break
            elif theBoard.get(str(0), "") == L and theBoard.get(str(4), "") == L and theBoard.get(str(8), "") == L:
                W += 1
                break
            elif theBoard.get(str(6), "") == L and theBoard.get(str(4), "") == L and theBoard.get(str(2), "") == L:
                W += 1
                break
            P1 += 1
            P3 += 3
        P1 = 0    
        P3 = 0
        L = "O"
    return W

def loop():
    global TT, T, V, W, WW, FBOARD
    pick()
    FBOARD = notes.get(T, 0)
    for V in range(1):
        try:
            if theBoard[FBOARD] == "X":
                loop()
            elif theBoard[FBOARD] == "O":
                loop()
            else:
                break
        except:
            loop()
            break
    theBoard[FBOARD] = TT
    win()
    babyboard()
    if W >= 1:
        print(">> The player ", TT, " WON!!!", sep="")
        sys.exit()
    if TT == "X":
        TT = "O"
    else:
        TT = "X"
    loop()

TT = "X"
T = ""
V = 0
W = 0
WW = ""
FBOARD = 0

P1 = 0
P3 = 0
L = ""
loop()
