import turtle

t = turtle.Turtle()

def square(length,color,positionX,positionY):
    t.screen.colormode(255)
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.goto(positionX,positionY)
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()

def rectangle(width,height,color,positionX,positionY):
    t.screen.colormode(255)
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.goto(positionX,positionY)
    for i in range(2):
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
    t.end_fill()


def triangle(length,color,positionX,positionY):
    t.screen.colormode(255)
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.goto(positionX,positionY)
    for i in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()