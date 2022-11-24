# Name:Tanishq Patil
import turtle
import math

def star_wrapper(n,d=2):
    alpha=180-((180*(n-2*d))/n)
    return alpha
  

def polygon(size,n):
    global t
    t.pendown()
    t.begin_fill()
    angle=360/n
    for i in range(n):
        t.forward(size)
        t.left(360/n)
    t.end_fill()
def polygon_recursive(size,n):
    global t
    global level2
    global beta
    t.pendown()
    if level2==0:
        beta=polygon_wrapper(size,n)
    if n!=0:
        t.forward(size)
        t.left(beta)
        level2+=1
        polygon_recursive(size,n-1)
    else:
        pass

def polygon_wrapper(size,n):
    b=360/n
    return b

def star(size,n,d=2):
    global t
    density=2
    winding=0
    for j in range(2,density):
        if density%j !=0:
            winding=j

    if n%2!=0:
        t.pendown()
        t.begin_fill()
        for i in range(n):
            t.forward(size)
            t.right(360/n)
            t.forward(size)
            t.left(density*360/n)
    else:   
        t.pendown()
        t.begin_fill()
        for i in range(n):
            t.forward(size)
            t.right(360/n)
            t.forward(size)
            t.left(density*360/n)

    t.end_fill()

def star_recursive(size,n,d=2):
    global t
    global alpha
    global level
    t.pendown()
    if level==0:
        alpha=star_wrapper(n,d=2)
    if n!=0:
        t.forward(size)
        t.left(alpha)
        level=level+1
        star_recursive(size,n-1, d=2)
    else:
        pass
def main(): ##  Driver Code
    global alpha
    global beta
    global level
    global level2
    global t
    alpha=0
    beta=0
    level=0
    level2=0
    s = turtle.Screen()     
    s.setup(400, 400)
    s.bgcolor("ivory4")
    s.title("Turtle Program")

    t = turtle.Turtle()     
    t.shape("turtle")  
    t.pen(pencolor='dark violet',fillcolor='dark violet', pensize=1, speed=0)

    t.penup()              
    t.goto(-100,50)   
    t.begin_fill
    star_recursive(25,7)    ##     Function Call
    t.end_fill()

    t.penup()               
    t.goto(100,-100)        
    t.color('gold')
    polygon_recursive(50, 5)    ##      Function Call

    t.penup()              
    t.goto(50,25)   
    t.begin_fill
        
    star(25,7)    ##     Function Call
    t.end_fill()

    t.penup()              
    t.goto(-20,0)   
    t.begin_fill
    
    polygon(25,8)    ##     Function Call
    t.end_fill()
main()


#Gloory glory hallelujah, glooory glory hallelujah, glooory glory hallelujah (his soul goes marching on)
#This assignment was difficult