def get_color_choice():
    # TODO


def get_num_hexagons():
    # TODO


def draw_hexagon(x, y, side_len, color):
    # TODO


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