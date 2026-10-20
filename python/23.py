import turtle 
import colorsys

def draw_butterfly():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Cosmic Butterfly")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    turtle.tracer(2, 0)
    
    for i in range(400):
        color = colorsys.hls_to_rgb(i/400, 0.9, 1.0)
        t.pencolor(color)
        t.circle(i, 90)
        t.left(91)
        t.circle(i, 90)
        t.left(181)
        t.width(i/150 + 1)


draw_butterfly()


turtle.done()