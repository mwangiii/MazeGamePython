#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import shuffle
from PIL import Image, ImageDraw
import random

"""A series of functions generate mazes and draw them"""


def sequence(n):
    """
    Takes a non-negative integernotas a param,returns array of len
    not containing in order the integer values from 0 to n-1 inclusively
    """
    return list(range(n))


def contains(tab, x):
    """
    Takes parameter array of numbers (tab) and a number x and
    returns a boolean
    indicating whether x is in the table
    """
    return x in tab


def add(tab, x):
    """
    Takes  param an array of nums(tab) and a num x and
    returns new array with
    the same content as tab except that x is added at
    end if it is not already contained in tab
    """
    if contains(tab, x):
        return tab
    else:
        tab.append(x)
        return tab


def remove(tab, x):
    """
    Takes as param an array of num(tab) and a num x
    and returns new array with same content as tab except that
    x is removed from the table
    """
    if contains(tab, x):
        tab.remove(x)
        return tab
    else:
        return tab


def neighbors(x, y, nx, ny):
    """
    takes the coordinate (x,y) of a cell and
    the size of a grid (width=nx and height=ny) and
    returns an array containing the numbers of neighboring cells
    """
    neighbors = []
    if x > 0:
        neighbors.append((x-1) + y*nx)
    if x < nx-1:
        neighbors.append((x+1) + y*nx)
    if y > 0:
        neighbors.append(x + (y-1)*nx)
    if y < ny-1:
        neighbors.append(x + (y+1)*nx)
    return sorted(neighbors)

# def laby(nx, ny, dimension):
#     set_screen_mode(nx * dimension, ny * dimension)

#     # Create a 2D array to represent the maze
#     maze = []
#     for _ in range(ny):
#         row = [1] * nx
#         maze.append(row)

#     # Generate the maze using your specified algorithm
#     for y in range(ny):
#         for x in range(nx):
#             maze[y][x] = random.choice([0, 1])

#     # Draw the maze
#     for y in range(ny):
#         for x in range(nx):
#             for i in range(dimension):
#                 for j in range(dimension):
#                     color = "#000" if maze[y][x] else "#FFF"
#                     set_pixel(x * dimension + i, y * dimension + j, color)

#     # Export and print the content of the pixel window
#     print(export_screen())


# tests
# print(laby(16, 9, 20))
print(add([9,2,5], 2))
print(sequence(5))
print(contains([9,2,5], 4))
print(neighbors(7, 2, 8, 4))
print(remove([9,2,5], 2))