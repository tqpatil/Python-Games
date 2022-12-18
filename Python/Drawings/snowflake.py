#Name:Tanishq Patil
import turtle
arr=[0,60,-120,60]
def koch(n,size):
    global t
    global arr
    if n == 0:
        t.forward(size)
    else:
        for i in arr:
            t.left(i)
            koch(size*(1/3), n-1)
def main():
    global t
    t=turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.pensize(2)
    s=turtle.Screen()
    s.setup(1000,1000,30,30)
    size=4
    koch(200, size) 
    t.right(120)
    koch(200, size)
    t.right(120)
    koch(200, size)
main()