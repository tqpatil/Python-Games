import random

board = [1,2,3,4,"X",6,7,8,9]

def displayBoard(board):
    print("    +-------+-------+-------+\n\
    |       |       |       |\n\
    |   "+str(board[0])+"   |   "+str(board[1])+"   |   "+str(board[2])+"   |\n\
    |       |       |       |\n\
    +-------+-------+-------+\n\
    |       |       |       |\n\
    |   "+str(board[3])+"   |   "+str(board[4])+"   |   "+str(board[5])+"   |\n\
    |       |       |       |\n\
    +-------+-------+-------+\n\
    |       |       |       |\n\
    |   "+str(board[6])+"   |   "+str(board[7])+"   |   "+str(board[8])+"   |\n\
    |       |       |       |\n\
    +-------+-------+-------+")

def EnterMove(board):
    input1 = input("Enter your move: ")
    if int(input1) in board:
        for i in range(len(board)):
            if board[i] == int(input1):
                board[i] = "O"
    else:
        print("Not Found")
          

def VictoryFor(board, sign):
    if (board[0] == sign and board[1] == sign and board[2] == sign or board[3] == sign and board[4] == sign and board[5] == sign or board[6] == sign and board[7] == sign and board[8] == sign or \
    board[0] == sign and board[3] == sign and board[6] == sign or board[1] == sign and board[4] == sign and board[7] == sign or board[2] == sign and board[5] == sign and board[8] == sign or \
    board[0] == sign and board[4] == sign and board[8] == sign or board[2] == sign and board[4] == sign and board[6] == sign):
        return True
    

def DrawMove(board):
    c = True
    while c:
        x = random.randrange(9)
        if x in board:
            for i in range(len(board)):
                if board[i] == x:
                    board[i] = "X"
                    c = False

val = True
displayBoard(board)
while val:
    EnterMove(board)
    if VictoryFor(board, "O"):
        print("Player Wins")
        displayBoard(board)
        break
    DrawMove(board)
    displayBoard(board)
    if VictoryFor(board, "X"):
        print("Computer Wins")
        break
               
        
