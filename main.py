import turtle
import math

def get_color_choice():
    # TODO


def get_num_hexagons():
    # TODO



def draw_hexagon(x, y, small_diag, color):
        turtle.showturtle()
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.speed(3)  # скорость для наглядности
        turtle.left(30)
        radian = math.radians(30)
        side_len = small_diag / 2 // math.cos(radian)
        turtle.fillcolor('{}'.format(color))
        turtle.begin_fill()
        turtle.forward(side_len)
        for i in range(5):
            turtle.right(60)
            turtle.forward(side_len)
        turtle.end_fill()
        turtle.right(90)


def tiling(number, color1, color2):
    color = ''
    for i in range(4):
        if i % 2 != 0:
            color = color1
        else:
            color = color2
        x += d
        draw_hexagon(d, color, x, y)


def main():
    # TODO


if __name__ == '__main__':
    main()