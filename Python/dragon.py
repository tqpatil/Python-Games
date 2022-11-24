#Name:Tanishq Patil
import turtle
list={}
for i in range(13):
    list[i]=[]
def create_direct(n):
    global list
    if n==12:
        list[0].append("R")
        create_direct(n-1)  ##  Recursive call
    elif n!=0 and n!=12:    ##  Base Case
        for i in range(len(list[12-(n+1)])):
            list[12-n].append(list[12-(n+1)][i])
        list[12-n].append("R")
        section=list[12-(n+1)].copy()
        section.reverse()
        for j in range(len(section)):
            if section[j]=="R":
                list[12-n].append("L")
            elif section[j]=="L":
                list[12-n].append("R")
        create_direct(n-1)  ##  Recursive Call




    
    
    
    
def draw_dragon(t,n=12):
    global list
    t.pendown()
    copy=[]

    for i in range(len(list[11])):
            if list[11][i]=="R":
                t.forward(5)
                t.right(90)
                
            if list[11][i]=="L":
                t.forward(5)
                t.left(90)
                
        
        

def main(): ## Driver Code
    s = turtle.Screen()     
    s.setup(400, 400)
    s.bgcolor("ivory4")
    s.title("Turtle Program")
    t = turtle.Turtle()    
    turtle.tracer(n=1, delay=0) 
    t.shape("turtle")  
    t.pen(pencolor='dark violet',fillcolor='dark violet', pensize=1, speed=0)
    t.penup()
    t.goto(0,100)
    level=0
    t.speed(0)
    create_direct(12)   ##      Function Call
    draw_dragon(t)  ##      Function Call
    turtle.done()
main()
#This one was very difficult too