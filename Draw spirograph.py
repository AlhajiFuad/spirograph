import random
import turtle

hajj = turtle.Turtle()
turtle.colormode(255)
turtle.title("SPIROGRAPH")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


hajj.speed("fastest")


def draw_spirograph(size):
    for _ in range(int(360 / size)):
        hajj.color(random_color())
        hajj.circle(108)
        hajj.setheading(hajj.heading() + 10)


draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()
