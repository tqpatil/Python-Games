#Name:Tanishq Patil
#File: fifteen.py
# Student ID:1961827 
#Date:11/29/2022
# Sources:Professor Munishkina, UCSC, Sample Code on Canvas   
# create the logic for the game Fifteen
import numpy as np
from graph import Vertex
from graph import Graph
import random

class Fifteen:

    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4): 
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        graph= Graph()
        verts=[]
        for i in range(len(self.tiles)):#Create the graph for the board
            if i==len(self.tiles)-1:
                graph.addVertex(i,0)
                break
            else:
                graph.addVertex(i,i+1)
        for j in range(len(self.tiles)):#add all the edges between each node
            leftedge=[0,4,8,12]
            rightedge=[3,7,11,15]
            if j not in rightedge and j<15:
                graph.addEdge(j,j+1)
            if j not in leftedge and j>0:
                graph.addEdge(j,j-1)
            if j<12:
                graph.addEdge(j,j+4)
            if j>3:
                graph.addEdge(j,j-4)

        self.graph=graph
            
        

        self.adj=[]
        self.size=size

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        print("+---+---+---+---+")#print out the game row by row
        if self.tiles[0]>9:
            stringy="|"
        else:
            stringy="| "
        arr=self.tiles[0:4]
        for i in range(len(arr)):
            adder=" | "
            if not i+1>=len(arr):
                if arr[i+1]>9:
                    adder=" |"
            

            stringy=stringy+str(arr[i])+adder
        print(stringy)
        print("+---+---+---+---+")#second row
        if self.tiles[4]>9:
            stringy="|"
        else:
            stringy="| "
        arr2=self.tiles[4:8]
        for i in range(len(arr2)):
            adder=" | "
            if not i+1>=len(arr2):
                if arr2[i+1]>9:
                    adder=" |"
            

            stringy=stringy+str(arr2[i])+adder
        print(stringy)
        print("+---+---+---+---+")#third row
        if self.tiles[8]>9:
            stringy="|"
        else:
            stringy="| "
        arr2=self.tiles[8:12]
        for i in range(len(arr2)):
            adder=" | "
            if not i+1>=len(arr2):
                if arr2[i+1]>9:
                    adder=" |"

            stringy=stringy+str(arr2[i])+adder
        print(stringy)
        print("+---+---+---+---+")#fourth row
        if self.tiles[12]>9:
            stringy="|"
        else:
            stringy="| "
        arr2=self.tiles[12:16]
        for i in range(len(arr2)):
            adder=" | "
            if not i+1>=len(arr2):
                if arr2[i+1]>9:
                    adder=" |"
            stringy=stringy+str(arr2[i])+adder
        print(stringy)
        print("+---+---+---+---+")



        
   


    # return a string representation of the vector of tiles as a 2d array  
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    #13 14 15 
    def __str__(self):#once again print out the lines row by row
        if self.tiles[0]>9:
            line="" 
        else:
            line=" "
        if self.tiles[4]>9:
            line2="" 
        else:
            line2=" "
        if self.tiles[8]>9:
            line3="" 
        else:
            line3=" "
        if self.tiles[12]>9:
            line4="" 
        else:
            line4=" "
        for i in range(len(self.tiles)):
            if i<4:
                if i==3:
                    if not i+1>len(self.tiles):#first row
                        if self.tiles[i+1]>9:
                            adder=" "
                        else:
                            adder="  "
                    line+=str(self.tiles[i])+adder
                else:
                    if not i+1>len(self.tiles):
                        if self.tiles[i+1]>9:
                            adder=" "
                        else:
                            adder="  "
                    line+=str(self.tiles[i])+adder
            if 3<i<8:#second row
                if i==7:
                    if not i+1>len(self.tiles):
                        if self.tiles[i+1]>9:
                            adder=" "
                        else:
                            adder="  "
                    line2+=str(self.tiles[i])+adder
                    
                    
                else:
                    if not i+1>len(self.tiles):
                        if self.tiles[i+1]>9:
                            adder=" "
                        else:
                            adder="  "
                    line2+=str(self.tiles[i])+adder
            if 7<i<12:#third row
                if i==11:
                    if not i+1>len(self.tiles):
                        if self.tiles[i+1]>9:
                            adder=" "
                        else:
                            adder="  "
                    line3+=str(self.tiles[i])+adder
                
                    
                else:
                    if not i+1>len(self.tiles):
                        if self.tiles[i+1]>9:
                            adder=" "
                        else:
                            adder="  "
                    line3+=str(self.tiles[i])+adder
            if 11<i<16:#fourth row
                if i==15:
                    if not i+1>=len(self.tiles):
                        if self.tiles[i+1]>9:
                            adder=" "
                        else:
                            adder="  "
                    line4+=str(self.tiles[i])+adder
                 
                    
                else: # FIX THE SPACING TO MATCH THE ASSERT
                    if not i+1>len(self.tiles):
                        if self.tiles[i+1]>9:
                            adder=" "
                        else:
                            adder="  "
                    line4+=str(self.tiles[i])+adder
        if (line[len(line)-2:len(line)])=="  ":
            copy=""
            for i in range(len(line)-1):
                copy+=line[i]
            line=copy
            copy=""
        if (line2[len(line2)-2:len(line2)])=="  ":
            copy=""
            for i in range(len(line2)-1):
                copy+=line2[i]
            line2=copy
            copy=""
        if (line3[len(line3)-2:len(line3)])=="  ":
            copy=""
            for i in range(len(line3)-1):
                copy+=line3[i]
            line3=copy
            copy=""
        if (line4[len(line4)-2:len(line4)])=="  ":
            copy=""
            for i in range(len(line4)-1):
                copy+=line4[i]
            line4=copy
            copy=""
        

            

        #Replace the zeroes with spaces
        return(line.replace(" 0","  ")+"\n"+line2.replace(" 0","  ")+"\n"+line3.replace(" 0","  ")+"\n"+line4.replace(" 0","  ")+"\n")


            


    # exchange i-tile with j-tile  
    # tiles are numbered 1-15, the last tile is 0 (empty space) 
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j): 
        key1=0
        key2=0
        for m in range(len(self.tiles)):
            if self.tiles[m]==i:
                key1=m
            if self.tiles[m]==j:
                key2=m
        self.tiles[key1]=j  #transpose on the game tiles array
        self.graph.getVertex(key1).setVal(j)#also transpose on the graph 
        self.tiles[key2]=i
        self.graph.getVertex(key2).setVal(i)
        
        return self.tiles
            
            
        


    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor 
    def is_valid_move(self, move): 
        if move>15 or move<1:
            return False
        val=0
        zPos=0
        for i in range(len(self.tiles)):
            if self.tiles[i]==move:
                val=i
            if self.tiles[i]==0:
                zPos=i
        leftedge=[0,4,8,12]
        rightedge=[3,7,11,15]
        if val+1==zPos and val not in rightedge:
            return True
        elif val-1==zPos and val not in leftedge:
            return True
        elif val+4==zPos:
            return True
        elif val-4==zPos:
            return True
        else:
            return False

        


    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose 
    def update(self, move): #updates the board if the given move is valid
        if self.is_valid_move(move):
            self.transpose(move,0)
        else:
            return
    
    # shuffle tiles
    def shuffle(self, moves = 100):
        leftedge=[0,4,8,12]
        rightedge=[3,7,11,15]
        index = np.where(self.tiles == 0)[0][0]
        posMoves=[]
        for i in range(moves):#Get all the possible moves at a given moment
            if index+1 not in rightedge and index+1<16:
                posMoves.append(index+1)
            if index-1 not in leftedge and index-1>=0:
                posMoves.append(index-1)
            if index<11:
                posMoves.append(index+4)
            if index>3:
                posMoves.append(index-4)
            move_index=random.choice(posMoves)#choose a random move
            posMoves=[]
            self.transpose(move_index,index)#make move
            # self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            # self.graph.getVertex(index).setVal(move_index)
            # self.graph.getVertex(move_index).setVal(index)
            index = move_index#continue until n moves have been made
    
    # verify if the puzzle is solved
    def is_solved(self):
       tilecopy = np.array([i for i in range(1,self.size**2)] + [0])
       thingy=True
       for i in range(len(tilecopy)):#check if the board is correct by comparing each value to a solved board
            if tilecopy[i]!=self.tiles[i]:
                thingy=False
       return thingy


    # verify if the puzzle is solvable (optional)
    def is_solvable(self):
        return True ##My shuffle only uses legal moves, so the implementation is in there

    # solve the puzzle (optional)
    def solve(self):
        index=0
        for i in range(len(self.tiles)):
            if self.tiles[i]==0:
                index=i
        cur=index
        prev=[]
        for j in range(80):
            if self.is_solved():
                break
            bfs=self.graph.breadth_first_search(cur)#use bfs to solve
            for k in range(1,len(bfs)):
                if self.is_valid_move(bfs[k]):
                    self.update(self.tiles[bfs[k]])
                    prev.append(cur)
                    cur=bfs[k]
                else:
                    count=len(prev)-1
                    while self.is_valid_move(bfs[k])==False and count>-1:
                        self.update(self.tiles[prev[count]])
                        cur=prev[count]
                        count=count-1
                        prev=prev[:count]
                    
                    





        ##ATTEMPT AT SOLVING EARLIER 
        # if self.is_solved()==True:
        #     print(moves)
        #     self.draw()
        #     return 1
        # index=0
        # leftedge=[0,4,8,1
        # rightedge=[3,7,11,15]
        # posMoves=[]
        # copy1=self
        # copy2=self
        # copy3=self
        # copy4=self
        # for i in range(len(self.tiles)):
        #     if self.tiles[i]==0:
        #         index=i
        # if index+1 not in rightedge and index+1<16:
        #     posMoves.append(index+1)
        # if index-1 not in leftedge and index-1>=0:
        #     posMoves.append(index-1)
        # if index<11:
        #     posMoves.append(index+4)
        # if index>3:
        #     posMoves.append(index-4)
        # for j in range(len(posMoves)):
        #     if j==0:
        #         moves.append(posMoves[j])
        #         self.update(posMoves[j])
        #         self.draw()
        #         self.solve(moves)
        #     if j==1:
        #         moves.append(posMoves[j])
        #         self.update(posMoves[j])
        #         self.draw()
        #         self.solve(moves)
        #     if j==2:
        #         moves.append(posMoves[j])
        #         self.update(posMoves[j])
        #         self.draw()
        #         self.solve(moves)
        #     if j==3:
        #         moves.append(posMoves[j])
        #         self.update(posMoves[j])
        #         self.draw()
        #         self.solve(moves)                

            


            



                    





if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    

    game = Fifteen()
    game.shuffle()
    game.solve()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
  