import turtle as t 
t.bgcolor("black")
t.pensize(1)
t.speed(0)
colors =["gold" , "blue"]
for i in range(300):
    t.color(colors[i%2])
    t.forward(i)
    t.right(91)

t.done()