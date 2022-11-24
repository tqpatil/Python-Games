import turtle

# draw a spiral
def draw_spiral(t, segments, size, angle):
    t.pendown()
    if segments+1>1:
        t.fd(size*segments)
        t.left(angle)
        draw_spiral(t,segments-1,size,angle)



# driver code
if __name__ == '__main__':
    s = turtle.Screen()
    s.setup(400, 400)
    t = turtle.Turtle()
    t.pen(pencolor='dark violet', pensize=2, speed=0)
    t.penup()
    t.home()
    draw_spiral(t, 80, 2, 92)