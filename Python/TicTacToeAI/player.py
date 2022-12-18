#Name:Tanishq Patil
#Student ID:1961827
#Player.py creates the "player" object and contains the "AI" object 
# including all necessary methods for making moves 
import board
import random
import math
class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            return self.sign
            # return an instance sign
      def get_name(self):
            return self.name
            # return an instance name
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty,update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ['A1', 'A2', 'A3', 'B1','B2','B3','C1','C2','C3']
            try:
                while True: 
                    cell = input(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:').upper().strip()
                    if cell in valid_choices :
                            if board.isempty(cell):
                                board.set(cell, self.sign)
                                break
                            else:
                                print("\nYou did not choose correctly.")
                    else:
                        print("You did not choose correctly.")
            except Exception:
                print("Something went wrong")               
class AI(Player):
    def __init__(self,name,sign,board):
        super().__init__(name,sign)
        self.board=board
            # return an instance name
    def choose(self,board):
        print(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
        x=0
        valid_choices = ['A1', 'A2', 'A3', 'B1','B2','B3','C1','C2','C3']
        valid=[]    #Get all valid moves
        while x<len(valid_choices):
            if board.isempty(valid_choices[x]):
                valid.append(valid_choices[x])
            x=x+1    

        x=random.choice(valid)  #pick a random move from the list of valid moves
        print(x)
        board.set(x,self.sign)
class SmartAI(AI):
    def __init__(self,name,sign,board):
        super().__init__(name,sign,board)
            # return an instance name
    def choose(self,board):
        valid_choices = ['A1', 'A2', 'A3', 'B1','B2','B3','C1','C2','C3']
        print(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:')
        x=self.bestMove(board)  #Get the best move depending on the board
        print(x)
        board.set(x,self.sign)
    def bestMove(self,board):
        
        valid_choices = ['A1', 'A2', 'A3', 'B1','B2','B3','C1','C2','C3']
        valid=[]    #Get a list of valid moves
        for i in range(len(valid_choices)):
            if board.isempty(valid_choices[i]):
                valid.append(valid_choices[i])
    
        
        if self.sign=="X":  #Get the sign of the other player
            other="O"
        else:
            other="X"
        for i in range(len(valid)):     #Determine if a move wins, then play it
            board.set(valid[i],self.sign)
            if board.get_winner()==self.sign:
                board.delete(valid[i])
                return valid[i]
            board.delete(valid[i])
        for i in range(len(valid)):     #If a move loses, then also play it
            board.set(valid[i],other)
            if board.get_winner()==other:
                board.delete(valid[i])
                return valid[i]
            board.delete(valid[i])

        emptySpaces=0   #Used to check which move it is
        for i in range(9):
            if board.isempty(valid_choices[i]):
                emptySpaces+=1
        if emptySpaces==9:  #If it is the first move, play One of the corners
            for i in range(len(valid)):
                if valid[i]=="A1":
                    return valid[i]
                elif valid[i]=="A3":
                    return valid[i]
                elif valid[i]=="C1":
                    return valid[i]
                elif valid[i]=="C3":
                    return valid[i]
        elif emptySpaces==8:    #If it is the second move, and the opponent has not played the center play the center 
            if "B2" in valid:
                return "B2"
            else:
                for i in range(len(valid)):     #Else, play a corner move
                    if valid[i]=="B2":
                        return "B2"
                    elif valid[i]=="A1":
                        return valid[i]
                    elif valid[i]=="A3":
                        return valid[i]
                    elif valid[i]=="C1":
                        return valid[i]
                    elif valid[i]=="C3":
                        return valid[i]
                
        elif emptySpaces<8:     #If it is not the first or second move, find a fork for you or the opponent
            x=self.fork(board)
            if x!="none":
                return x
            else:
                for i in range(len(valid)):     #If no forks exist, play either a corner, or the next available move 
                    if valid[i]=="A1":
                        return valid[i]
                    elif valid[i]=="A3":
                        return valid[i]
                    elif valid[i]=="C1":
                        return valid[i]
                    elif valid[i]=="C3":
                        return valid[i]
                for i in range(len(valid)):
                    return valid[i]

        else:
            for i in range(len(valid)): #If all else fails, play either a corner or any available move 
                if valid[i]=="A1":
                    return valid[i]
                elif valid[i]=="A3":
                    return valid[i]
                elif valid[i]=="C1":
                    return valid[i]
                elif valid[i]=="C3":
                    return valid[i]
            for i in range(len(valid)):
                return valid[i]

        
    
            


    def fork(self,board):
        valid_choices = ['A1', 'A2', 'A3', 'B1','B2','B3','C1','C2','C3']
        valid=[]    #generate valid moves
        j=0
        while j<len(valid_choices):
            if board.isempty(valid_choices[j]):
                valid.append(valid_choices[j])
            j=j+1
        j=0

        if self.sign=="X":  #Get Signs
            other="O"
        else:
            other="X"
        forkMove="None"
        for i in range(len(valid)):     #iterates through valid moves and looks for a fork
            x=board.numWins(valid[i],self.sign)
            if x>1:
                forkMove= valid[i]
        if forkMove=="None":
            for k in range(len(valid)):
                x=board.numWins(valid[k],other) #If the number of ways to win after playing a move 
                if x>1:                         #is more than 1, we found a fork!
                    forkMove=valid[k]
        if forkMove=="None":        #else, there is no fork
            return "none"
        else:
            return forkMove #return the forking move

            


        

class MiniMax(AI):
    def __init__(self,name,sign,board): #initializer
        super().__init__(name,sign,board)
    def choose(self,board):#overridden choose method
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell =self.bestMove(board)  #gets the best move using recursive minimax
        print(cell)
        board.set(cell, self.sign)

    def minimax(self, board, self_player, start):
        if self.sign=="X":  #gets player and opponent signs
            other="O"
        else:
            other="X"
        valid_choices = ['A1', 'A2', 'A3', 'B1','B2','B3','C1','C2','C3']
        x=board.isdone()    #terminating condition
        if x:
            win=board.get_winner()
            if win==self.sign:  #win
                board.resetWinner()
                return 1
            elif "tie" == win:  #tie
                board.resetWinner()
                return 0
            elif win==other:    #loss
                board.resetWinner()
                return -1
        if self_player:     #If it is your turn, you want to maximize your score
            higher=-1000    #placeholder for score
            
            for i in range(9):
                if board.isempty(valid_choices[i]): #Only use possible moves
                    board.set(valid_choices[i],self.sign)
                    higher=max(higher,self.minimax(board,not self_player,False))    #Recursive Call
                    board.delete(valid_choices[i])
            return higher
        else:   #if it is the opponents turn, you want to minimize their score
            higher=1000 #placeholder for score
            for i in range(9):
                if board.isempty(valid_choices[i]): #Only use possible moves
                    board.set(valid_choices[i],other)
                    higher=min(higher,self.minimax(board, not self_player, False))  #Recursive Call
                    board.delete(valid_choices[i])
            return higher
    def bestMove(self,board):   #Uses minimax for each move 
        valid_choices = ['A1', 'A2', 'A3', 'B1','B2','B3','C1','C2','C3']
        bestVal=-10000
        bestMove=-10000
        for i in range(9):  #Cycles through all possible moves 
            if board.isempty(valid_choices[i]):
                board.set(valid_choices[i],self.sign)
                moveVal=self.minimax(board,False,True)  #gets minimax score for the move
                board.delete(valid_choices[i])
                if moveVal>bestVal: #Takes the higher score move between the previous move and new score
                    bestMove=valid_choices[i]   
                    bestVal=moveVal
        return bestMove #returns the move with the highest score from minimax

        

        
        
            


        







