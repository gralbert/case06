import turtle
import math


def get_color_choice(color):
    new_color = ''
    stand_color = ' ' + color.lower() + ' '
    while stand_color not in ' желтый красный зеленый синий ' \
                             'оранжевый пурпурный розовый зелёный жёлтый ':
        color = input('{} не является верным значением. '
                      'Пожалуйста, повторите попытку: '.format(color))
        stand_color = ' ' + color.lower() + ' '
    else:
        if stand_color in ' желтый жёлтый ':
            new_color = 'yellow'
        elif stand_color in ' зеленый зелёный ':
            new_color = 'green'
        elif stand_color in ' красный ':
            new_color = 'red'
        elif stand_color in ' синий ':
            new_color = 'blue'
        elif stand_color in ' оранжевый ':
            new_color = 'orange'
        elif stand_color in ' пурпурный ':
            new_color = 'purple'
        elif stand_color in ' розовый ':
            new_color = 'pink'
        return new_color


def get_num_hexagons():
    number_of_polygons = input('Пожалуйста, введите '
                               'количество шестиугольников, располагаемых в ряд: ')
    while True:
        if not number_of_polygons.isdigit():
            number_of_polygons = input('Оно должно быть от 4 до 20.'
                                       ' Пожалуйста, повторите попытку: ')
        elif not(4 <= int(number_of_polygons) <= 20):
            number_of_polygons = input('Оно должно быть от 4 до 20.'
                                       ' Пожалуйста, повторите попытку: ')
        else:
            break
    return int(number_of_polygons)


def draw_hexagon(x, y, side_len, color):
    turtle.showturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.speed(0)  # скорость для наглядности
    turtle.left(30)
    turtle.fillcolor('{}'.format(color))
    turtle.begin_fill()
    turtle.forward(side_len)
    for i in range(5):
        turtle.right(60)
        turtle.forward(side_len)
    turtle.end_fill()
    turtle.right(90)


def tiling(number, color1, color2):
    y = 250
    x = -300
    small_diag = 500 // number
    radian = math.radians(30)
    side_len = small_diag / 2 // math.cos(radian)
    count = 0
    for j in range(number):
        for i in range(number):
            if i % 2 != 0:
                color = color1
            else:
                color = color2
            x += small_diag
            draw_hexagon(x, y, side_len, color)
        turtle.penup()
        turtle.left(180)
        if j % 2 != 0:
            turtle.forward(small_diag * number - 0.5 * small_diag)
        else:
            turtle.forward(small_diag * number + 0.5 * small_diag)
        turtle.left(90)
        turtle.forward(side_len * 1.5)
        turtle.left(90)
        x = float(str(turtle.position())[str(turtle.position())
                  .find('(') + 1:str(turtle.position()).find(',')])
        y = float(str(turtle.position())[str(turtle.position())
                  .find(',') + 1:str(turtle.position()).find(')')])
        count += 1
        if count == 2:
            color1, color2 = color2, color1
            count = 0
    turtle.done()


def main():
    print('Допустимые цвета заливки:  красный, синий, зеленый,'
          ' желтый, оранжевый, пурпурный, розовый.')
    first_color = str(input('Пожалуйста, введите первый цвет: '))
    col_1 = get_color_choice(first_color)
    second_color = str(input('Пожалуйста, введите второй цвет: '))
    col_2 = get_color_choice(second_color)
    num_hex = get_num_hexagons()
    tiling(num_hex, col_1, col_2)


if __name__ == '__main__':
    main()
