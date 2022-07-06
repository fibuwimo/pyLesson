import turtle
t=turtle.Turtle()
t.shape('turtle')
for i in range(1000):
    t.right(i)
    t.forward(i)
turtle.mainloop()
