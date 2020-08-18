import turtle
#import time
a=turtle.Turtle()
b=turtle.Turtle()
a.pensize(10)
a.color('red')
b.pensize(5)
b.color('blue')
for i in range(360):
    a.forward(1)
    a.left(1)
    b.forward(1)
    b.right(1)
turtle.done()

