import turtle
import colorsys

def draw_starburst():

    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Lab Activity 1 - Creative Geometric Starburst")

    t = turtle.Turtle()
    t.speed(0)
    turtle.colormode(255)
    t.hideturtle()

    num_lines = 120

    print("Drawing creative starburst... Please wait!")

    for i in range(num_lines):

        hue = i / num_lines
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        r = int(rgb[0] * 255)
        g = int(rgb[1] * 255)
        b = int(rgb[2] * 255)

        t.pencolor(r, g, b)
        t.pensize(i // 30 + 1)


        t.forward(i * 3)
        t.left(145)
        t.forward(i * 1.5)
        t.right(45)

    screen.exitonclick()

if __name__ == "__main__":
    draw_starburst()