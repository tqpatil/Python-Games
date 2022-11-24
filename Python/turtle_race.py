# turtle race
from turtle import *
from random import randint
import turtle

def set_turtles(colors):
    turtles = []
    for color in colors:
        t = Turtle()
        t.color(color)
        t.shape("turtle")
        t.speed(1)
        turtles.append(t)
    return turtles

def draw_track(start, finish):
    t = Turtle()
    t.speed(0)
    position, size, step = 100, 200, 40
    count = 0
    for line in range(start, finish + step, step):
        t.penup()
        t.goto(line,position+10)
        if line == start:
            t.color("blue")
            t.pensize(10)
            t.write("START")
        elif line == finish:
            t.color("red")
            t.pensize(10)
            t.write("FINISH")
        else:
            t.color("grey")
            t.pensize(1)
            t.write(count)
        t.goto(line,position)
        count += 1
        t.right(90)
        t.pendown()
        t.forward(size)
        t.left(90)
    
def isfinish(t, finish):
    x, y = t.pos()
    if x < finish:
        return False
    else:
        return True

def race(start, finish):
    global turtles
    global s
    # y position
    position = 80
    distance = 40
    turtles[0].penup()
    turtles[0].left(180)
    turtles[0].goto(start,position)
    turtles[1].penup()
    turtles[1].left(180)
    turtles[1].goto(start,position-80)
    turtles[0].left(180)
    turtles[1].left(180)
    done=False
    while not done:
        onscreenclick(move)
        turtles[1].forward(randint(1,10))
        if isfinish(turtles[0],finish) :
            x=1
            done=True
        elif isfinish(turtles[1],finish):
            x=2
            done=True
    s.clear() 
    t=turtle.Turtle()
    t.hideturtle
    if x==1:
        t.write("Congratulations, you won!")
    elif x==2:
        t.write("Sorry! Try Again")
    turtle.done()
    



def click(t):
    onscreenclick(None,move)
def move(x,y):
    global turtles
    turtles[0].forward(10)
def clear(x,y):
    global s
    s.clear()
# main program
s = Screen()     # make a canvas window
s.setup(500, 400)
s.bgcolor("white")
s.title("Turtle Race")
thingy=turtle.Turtle()
thingy.penup()
thingy.goto(0,150)
thingy.write("tip:use your left mouse button to move the turtle!")
start = -200  # x position
finish = 200  # x position
turtles = set_turtles(["yellow", "crimson"])
draw_track(start, finish)

race(start, finish)
