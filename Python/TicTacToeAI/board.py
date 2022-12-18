#Name:Tanishq Patil
#Student ID:1961827
#Board.py creates the game board and contains all necessary methods for checking and using the board
class Board:
    def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)           # the winner's sign O or X
            self.winner = ""
    def get_size(self): 
        pass
            # optional, return the board size (an instance size)
    def get_winner(self):
        valid_choices = ['A1', 'A2', 'A3', 'B1','B2','B3','C1','C2','C3']
        wContainer=" " #Contains winning player's sign
        winnerExists=False
        win=[[0,1,2], [3,4,5], [6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #List of all win conditions
        for i in range(len(win)):   #loops through win conditions
            if self.board[win[i][0]]==self.board[win[i][1]]==self.board[win[i][2]]!= " ":#If a win condition is met
                wContainer=self.board[win[i][0]].strip()    #return the winner
                winnerExists=True

        if " " not in self.board and winnerExists==False:   #If the board is full and there was no winner set
            wContainer="tie"# it is a tie
        if " " in self.board and winnerExists==False:   #otherwise, the game has not ended
            wContainer=" "

        



        return wContainer

            

    def get_board(self):    #returns the board
        return self.board
    def isFull(self):   #checks if all spaces in the board are taken
        for i in range(len(self.board)):
            if i=="" or " ":
                return False
        return True
    def setEntireBoard(self,strboard):  #Used for debugging: sets the entire board to a new list 
        self.board=strboard

 
    def set(self, cell, sign):  #Sets a cell to a sign
        alph={"A1":1, "A2":4, "A3":7, "B1":2, "B2":5,"B3":8, "C1":3, "C2":6, "C3":9}
        x=cell.upper().strip()
        self.board[alph[x]-1]=sign
        # mark the cell on the board with the sign X or O
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # you can use a tuple ("A1", "B1",...) to obtain indexes 
        # this implementation is up to you 
    def isempty(self, cell):    #checks if a cell is empty
        alph={"A1":1, "A2":4, "A3":7, "B1":2, "B2":5,"B3":8, "C1":3, "C2":6, "C3":9}
        x=cell.upper().strip()
        if self.board[alph[x]-1]==" " or "":# return True if the cell is empty (not marked with X or O)
            return True
        elif "O" or "X" in self.board[alph[x]-1]:#else return false
            return False
            

    def isdone(self):   #checks if the game is over and sets the winner
        valid_choices = ['A1', 'A2', 'A3', 'B1','B2','B3','C1','C2','C3']
        done = False
        x=self.get_winner() #gets the winner

        if "O" or "X" in (x):   
            self.winner=x.upper().strip()   #sets the board winner
            done=True
        if x=="tie":
            done=True
            self.winner="tie"
        if x==" ":  #the game is not over if get_winner() returns a space
            done=False

        
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X
        return done
    def numWins(self,cell,sign):#Counts the number of possible wins a move creates(used to look for doubles)
        valid_choices = ['A1', 'A2', 'A3', 'B1','B2','B3','C1','C2','C3']
        wins=0
        self.set(cell,sign)#pass a valid cell that you know has an empty space or issues will occur
        valid=[]
        for i in range(len(valid_choices)): #gets and stores all valid moves
            if self.isempty(valid_choices[i]):  
                valid.append(valid_choices[i])
        for i in range(len(valid)): #loops through valid moves and checks if the given sign receives a win
            self.set(valid[i],sign)
            if self.get_winner()==sign:
                wins+=1     #increment the number of wins a move creates
                self.delete(valid[i])
            else:
                self.delete(valid[i])
        self.delete(cell)
        return wins

    
        

    def delete(self,cell):  #used for resetting a cell 
        alph={"A1":1, "A2":4, "A3":7, "B1":2, "B2":5,"B3":8, "C1":3, "C2":6, "C3":9}
        self.board[alph[cell]-1]=" "
    def resetWinner(self):  #Used for resetting the winner
        self.winner=""
    def show(self): #prints the board
        print('\n   A   B   C') 
        print(' +---+---+---+')
        print('1| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]))   
        print(' +---+---+---+')
        print('2| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5]))
        print(' +---+---+---+')
        print('3| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8]))
        print(' +---+---+---+')

