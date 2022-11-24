# draws a tree
import turtle
import random

# set the canvas window
def set_canvas():
    s = turtle.Screen()     
    s.setup(450, 410)
    s.bgcolor('ivory')
    s.title('Turtle Program')
    return s

# set a turtle (a pen)
def set_pen(color):         
    t = turtle.Turtle()
    t.shape('turtle')  
    t.pen(pencolor=color,fillcolor=color, pensize=1, speed=10)
    return t

# draw a tree fractal using recursion
def draw_tree(t, branch, angle, n):
  if n > 0: # recursive step
        t.color('red')
        t.pensize(n)
        t.forward(branch+random.randint(0,10))
        length = branch * 9/10
        t.left(angle)
        draw_tree(t, length, angle, n-1) # recursive call (left branch of the tree)
        t.color('red')
        t.right((angle * 2)+random.randint(0,10)/10)
        t.pensize(n)
        t.forward(branch/10)
        draw_tree(t, length, angle+random.randint(0,10), n-1) # recursive call (right branch of the tree)
        t.color('red')
        t.left(angle)
        t.backward(branch*1.1)
  else: # base case
        t.color('green')
        t.pendown()
        t.dot(15)

# main program 
def main():
    s = set_canvas()
    t = set_pen('black')
    t.penup()
    t.goto(-45, -150)
    t.left(90)
    t.pendown()
    t.begin_fill()
    draw_tree(t, 60, 20, 6)
    t.end_fill()
main()