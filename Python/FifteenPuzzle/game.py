#Name:Tanishq Patil
#File: game.py
# Student ID:1961827 
#Date:12/4/2022
# Sources:Professor Munishkina, UCSC, Sample Code on Canvas   
# create a GUI game of Fifteen

from tkinter import *
import tkinter.font as font

from fifteen import Fifteen
buttons=[]
def calculator(gui):   
    global fifteen
    global buttons
    # name the gui window
    gui.title("15")
    if len(buttons)==0:#if the buttons are not already initialized

        b0 = addButton(gui," ")
        b1 = addButton(gui,'1')
        b2 = addButton(gui,'2')
        b3 = addButton(gui,'3')
        b4 = addButton(gui,'4')
        b5 = addButton(gui,'5')
        b6 = addButton(gui,'6')
        b7 = addButton(gui,'7')
        b8 = addButton(gui,'8')
        b9 = addButton(gui,'9')
        b10 = addButton(gui,'10')
        b11 = addButton(gui,'11')
        b12 = addButton(gui,'12')
        b13 = addButton(gui,'13')
        b14 = addButton(gui,'14')
        b15 = addButton(gui,'15')
        shuffle=addButton(gui,"shuffle")#initialize the buttons


        # add buttons to the grid
        buttons=[b1, b2, b3 ,b4,
                b5, b6, b7, b8,
                b9, b10, b11, b12,
                b13,b14,b15,b0,shuffle]
    k = 4         
    for i in range(k):
        for j in range(k):
            buttons[i*k+j].grid(row=i+1, column=j, columnspan=1)
    buttons[16].grid(row=5,column=1,columnspan=1)#grid the buttons
  
def addButton(gui, value):#add button function, global variable for the board object
    global fifteen
    return Button(gui, text=value, height=4, width=9, command = lambda: clickButton(value))

def clickButton(value):#global board object, all the buttons, and the gui
    global fifteen
    global buttons
    global gui
    index=0
    if value=="shuffle":#shuffle the board if the user clicks "shuffle"
        fifteen.shuffle()
        newboard=fifteen.tiles
        newboard=[" " if i ==0 else i for i in newboard]#reinitialize the buttons to update the board
        b0 = addButton(gui,str(newboard[15]))
        b1 = addButton(gui,str(newboard[0]))
        b2 = addButton(gui,str(newboard[1]))
        b3 = addButton(gui,str(newboard[2]))
        b4 = addButton(gui, str(newboard[3]))
        b5 = addButton(gui,str(newboard[4]))
        b6 = addButton(gui,str(newboard[5]))
        b7 = addButton(gui,str(newboard[6]))
        b8 = addButton(gui,str(newboard[7]))
        b9 = addButton(gui,str(newboard[8]))
        b10 = addButton(gui,str(newboard[9]))
        b11 = addButton(gui,str(newboard[10]))
        b12 = addButton(gui,str(newboard[11]))
        b13 = addButton(gui,str(newboard[12]))
        b14 = addButton(gui,str(newboard[13]))
        b15 = addButton(gui,str(newboard[14]))
        shuffle=addButton(gui,"shuffle")
        buttons=[b1, b2, b3 ,b4,
                b5, b6, b7, b8,
                b9, b10, b11, b12,
                b13,b14,b15,b0,shuffle]
        calculator(gui)


               # add buttons to the grid
        
        
    for i in range(len(buttons)):
        if buttons[i].cget('text')==" ":
            index=i
    if value!=" " and value!="shuffle":
        if fifteen.is_valid_move(int(value)):
            newboard=fifteen.transpose(int(value),0)
            newboard=[" " if i ==0 else i for i in newboard]#make the move on the gui board by reinitializing the buttons
            b0 = addButton(gui,str(newboard[15]))
            b1 = addButton(gui,str(newboard[0]))
            b2 = addButton(gui,str(newboard[1]))
            b3 = addButton(gui,str(newboard[2]))
            b4 = addButton(gui, str(newboard[3]))
            b5 = addButton(gui,str(newboard[4]))
            b6 = addButton(gui,str(newboard[5]))
            b7 = addButton(gui,str(newboard[6]))
            b8 = addButton(gui,str(newboard[7]))
            b9 = addButton(gui,str(newboard[8]))
            b10 = addButton(gui,str(newboard[9]))
            b11 = addButton(gui,str(newboard[10]))
            b12 = addButton(gui,str(newboard[11]))
            b13 = addButton(gui,str(newboard[12]))
            b14 = addButton(gui,str(newboard[13]))
            b15 = addButton(gui,str(newboard[14]))
            shuffle=addButton(gui,"shuffle")


            # add buttons to the grid
            buttons=[b1, b2, b3 ,b4,
                    b5, b6, b7, b8,
                    b9, b10, b11, b12,
                    b13,b14,b15,b0,shuffle]
        
        calculator(gui)
        if fifteen.is_solved():#create a new popup window when the user successfully completes the game
            thing=Tk()
            thing.geometry("500x500")
            l = Label(thing, text = "YOU WIN",bg="pink")
            l.config(font =("Courier", 40))
            l.pack()
            thing.mainloop()
        


    
    
   ## print(value) # for debugging
    
# main program
# create the main window
gui = Tk()
fifteen=Fifteen()
calculator(gui)
# update the window
gui.mainloop()