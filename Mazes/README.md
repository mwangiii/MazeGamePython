#  PRACTICLE WORK

## ABOUT 
Here we try to create a maze using python

## BRAINSTORMING
width = len of horizontal cells(nx)
height =   len of vertical cells (ny)
North, East, South, and West walls (to simplify N, E, S,W) of the cell
n is the number of cells
nx is number of columns 
ny is number of rows
N = x + y * nx
E = 1 + x + y * (nx+1) 
S = x +(y+1) * nx
w = x + y * (nx+1)
certaindimension(the width and height of each square cell, in number of pixels between the
walls)
**The maze is therefore created by eliminating certain walls from the grid.**
 The outer wall of the grid is pierced at the top left (the entrance to the maze) and the bottom right (the exit from the maze)
use uses random numbers to create the maze but ensures that there is always exactly one path between entering and exiting the maze
there is always exactly one path between any cell and any other cell (formally
called an underlying tree)
horizontal = not removed
vertical = removed