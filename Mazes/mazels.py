#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import shuffle
from PIL import Image, ImageDraw
import random
import unittest

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




class TestMazeFunctions(unittest.TestCase):
    """tests for maze.py"""

    def test_sequence(self):
        """Test case for sequence function"""
        result = sequence(5) 
        self.assertEqual(result, [0, 1, 2, 3, 4])

    def test_contains(self):
        """Test case for contains function - positive case"""
        result_positive = contains([1, 2, 3], 2)
        self.assertTrue(result_positive)

        """Test case for contains function - negative case"""
        result_negative = contains([1, 2, 3], 4)
        self.assertFalse(result_negative)

    def test_add(self):
        """Test case for add function"""
        result = add([9, 2, 5], 2) 
        self.assertEqual(result, [9, 2, 5])

    def test_remove(self):
        """Test case for remove function"""
        result = remove([1, 2, 3], 2)
        self.assertEqual(result, [1, 3])

    def test_neighbors(self):
        """Test case for neighbors function"""
        result = neighbors(7, 2, 8, 4)
        self.assertEqual(result, [15, 22, 31])



if __name__ == "__main__":
    unittest.main()
