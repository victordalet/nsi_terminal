import turtle

t = turtle.Turtle()
t.speed(0)


##################### function that positions the cursor and sets the color of the platform #####################
def initialization(positionX,positionY,color):
    t.up()
    t.goto(positionX, positionY)
    t.down()
    t.screen.colormode(255)
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()

##################### function that creates squares #####################
def square(length,color,positionX,positionY):
    initialization(positionX, positionY, color)
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()

##################### function that creates rectangle #####################
def rectangle(width,height,color,positionX,positionY):
    initialization(positionX, positionY, color)
    for i in range(2):
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
    t.end_fill()

##################### function that creates rounded_rectangle #####################
def rounded_rectangle(width,color,positionX,positionY):
    initialization(positionX,positionY,color)
    t.forward(width)
    t.left(90)
    t.forward(width)
    t.circle(15,180)
    t.forward(width)
    t.left(90)
    t.end_fill()

##################### function that creates triangle for the roof #####################
def triangle(color,positionX,positionY):
    initialization(positionX, positionY, color)
    t.backward(5)
    t.left(90)
    t.forward(5)
    t.right(65)
    t.forward(82)
    t.right(50)
    t.forward(82)
    t.right(65)
    t.forward(5)
    t.left(90)
    t.backward(150)
    t.end_fill()

