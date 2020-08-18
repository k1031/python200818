import turtle
x=int(input('請輸入有幾個邊:'))
a=turtle.Turtle()
for i in range(x):
    a.forward(100)
    a.left(360/x)
turtle.done()

