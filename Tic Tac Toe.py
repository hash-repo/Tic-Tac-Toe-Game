# welcome to Tic Tac Toe Game Designed By Ahmed Hashish
def BoardDisplay(XO):
    print('-------------')
    print('| '+XO[6]+' | '+XO[7]+' | '+XO[8]+' |')
    print('-------------')
    print('| '+XO[3]+' | '+XO[4]+' | '+XO[5]+' |')
    print('-------------')
    print('| '+XO[0]+' | '+XO[1]+' | '+XO[2]+' |')
    print('-------------')
def wintest(XO,LastSymbolAdded):
    win=False

    for i in range(0,7,3): # Check Rows
        if XO[i:i+3]==[LastSymbolAdded]*3 and win==False: win=True
    for i in range(0,3): # Check Columns
        if XO[i:i+7:3]==[LastSymbolAdded]*3 and win==False: win=True
    for i in range(0,3,2): # Check Diagonals
        if XO[i:9-i:4-i]==[LastSymbolAdded]*3 and win==False: win=True

    return win

XO=[' ']*9
Name=['Player1','Player2']
Symbol=['X','O']
for i in [0,1]:
    Name[i] = input("Player"+str(i+1)+" with Symbol \'"+Symbol[i]+"\' Name is:")

turn=1
for i in range(0,8):
    I=1
    while I:
        Loc=int(input(Name[turn-1]+" with symbol \'"+Symbol[turn-1]+"\' choose your location on Board from 1 to 9:"))
        if Loc in range(1,10):
            if XO[Loc-1]==' ':
                XO[Loc-1]=Symbol[turn-1]
                BoardDisplay(XO)
                I=0
                turn=3-turn
    if wintest(XO,XO[Loc-1]):
        print('Congratulations ' + Name[3-turn-1] +'\nYou won ********')
        break
else:
    print('Draw ----> No Winner')
