from random import shuffle
from turtle import *

def generate_labyrinth(nx, ny):
    """
    Takes the size of a grid (width=nx and height=ny) and
    returns the walls of the labyrinth
    """
    nb_cell = nx * ny
    walls_h = sequence(nx * (ny + 1) - 1)
    walls_h = remove_element(walls_h, 0)
    walls_v = sequence((nx + 1) * ny)

    cell_v = []
    v_in_cave = []
    neighbor = 0

    random_cell = random.randint(0, nb_cell - 1)
    coord_c = coordinates_cell(random_cell, nx)
    coord_cx, coord_cy = coord_c[0], coord_c[1]

    cave = [random_cell]
    front = neighbors(coord_cx, coord_cy, nx, ny)

    for nb_elements_cave in range(1, nb_cell):
        random_cell = front[random.randint(0, len(front) - 1)]

        front = remove_element(front, random_cell)
        cave = add_element(cave, random_cell)

        coord_c = coordinates_cell(random_cell, nx)
        coord_cx, coord_cy = coord_c[0], coord_c[1]

        cell_v = neighbors(coord_cx, coord_cy, nx, ny)
        v_in_cave = [neighbor for neighbor in cell_v if neighbor in cave]

        for neighbor in cell_v:
            if neighbor in cave:
                v_in_cave.append(neighbor)
            else:
                front = add_element(front, neighbor)

        coord_v = coordinates_cell(v_in_cave[random.randint(0, len(v_in_cave) - 1)], nx)
        coord_vx, coord_vy = coord_v[0], coord_v[1]

        if coord_cx == coord_vx:
            if coord_cy == coord_vy + 1:
                walls_h = remove_element(walls_h, random_cell)
            else:
                walls_h = remove_element(walls_h, random_cell + nx)
        else:
            if coord_cx == coord_vx - 1:
                walls_v = remove_element(walls_v, coord_vx + coord_vy * (nx + 1))
            else:
                walls_v = remove_element(walls_v, coord_vx + 1 + coord_vy * (nx + 1))

    walls = [walls_h, walls_v]
    return walls


def draw_wall(x, y, orientation, step):
    """
    Takes the coordinates (x, y) of a wall,
    its orientation ('H' for horizontal, 'V' for vertical),
    and the step of the cell, and
    draws the wall
    """
    penup()
    goto(x, y)
    pendown()

    if orientation == 'H':
        forward(step)
    elif orientation == 'V':
        right(90)
        backward(step)
        right(90)


def draw_labyrinth(walls_h, walls_v, nx, ny, step):
    """
    Takes the walls of the labyrinth and
    the size of a grid (width=nx and height=ny) and
    the step of the cell and
    draws the labyrinth
    """
    x0 = -nx * step / 2
    y0 = ny * step / 2

    # Draw vertical walls
    for i in range(len(walls_v)):
        wall_indv = walls_v[i]
        x = x0 + wall_indv % (nx + 1) * step
        y = y0 + (wall_indv // (nx + 1)) * -step
        draw_wall(x, y, 'V', step)

    # Draw horizontal walls
    for i in range(len(walls_h)):
        wall_indh = walls_h[i]
        x = x0 + (wall_indh % nx) * step
        y = y0 + (wall_indh // nx) * -step
        draw_wall(x, y, 'H', step)


labyrinth(16, 9, 20)
turtle.mainloop()
