def koch(length, limit):
    if length<limit:
        turtle.forward(length)
    else:
        koch(length/3, limit)
        turtle.left(60)
        koch(length/3, limit)
        turtle.right(120)
        koch(length/3, limit)
        turtle.left(60)
        koch(length/3, limit)
            
import turtle
turtle.setup(width=500, height=500)
turtle.up()
turtle.backward(250)
turtle.down()
turtle.tracer(True)
koch(500,1)
turtle.done()
