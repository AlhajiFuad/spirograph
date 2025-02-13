import random
import turtle

# Set up the turtle and screen
hajj = turtle.Turtle()
turtle.colormode(255)
turtle.title("SPIROGRAPH")

def random_color():
    """Generate a random RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

hajj.speed("fastest")

def draw_spirograph(size, radius):
    """
    Draw a spirograph with the given size increment and circle radius.
    :param size: The angle increment for each circle.
    :param radius: The radius of the circles.
    """
    for _ in range(int(360 / size)):
        hajj.color(random_color())
        hajj.circle(radius)
        hajj.setheading(hajj.heading() + size)

if __name__ == "__main__":
    # Customize spirograph parameters
    spirograph_size = 5  # Angle increment in degrees
    spirograph_radius = 108  # Circle radius

    # Draw the spirograph
    draw_spirograph(spirograph_size, spirograph_radius)

    # Exit on click
    screen = turtle.Screen()
    screen.exitonclick()