def get_color_choice():
    new_color = ''
    stand_color = ' ' + color.lower() + ' '
    while stand_color not in ' желтый красный зеленый синий оранжевый пурпурный розовый зелёный жёлтый ':
        color = input("'{}' не является верным значением. Пожалуйста, повторите попытку: ".format(color))
        stand_color = ' ' + color.lower() + ' '
    else:
        if stand_color in " желтый жёлтый ":
            new_color = "yellow"
        elif stand_color in " зеленый зелёный ":
            new_color = "green"
        elif stand_color in " красный ":
            new_color = "red"
        elif stand_color in " синий ":
            new_color = "blue"
        elif stand_color in " оранжевый ":
            new_color = "orange"
        elif stand_color in " пурпурный ":
            new_color = "purple"
        elif stand_color in " розовый ":
            new_color = "pink"
        return new_color


def get_num_hexagons():
    # TODO


def draw_hexagon(x, y, side_len, color):
    # TODO


def tiling(number, color1, color2):
    # TODO


def main():
    # TODO


if __name__ == '__main__':
    main()