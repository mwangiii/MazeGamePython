#  PRACTICLE WORK

## ABOUT 
Here we try to create a maze using python

## REQUIREMENTS
### Task Requirements Outline

#### Functions to Create:
1. **sequence(n) function**
   - Input: Non-negative integer n
   - Output: Array of length n containing values from `0` to `n-1`
   
2. **contains(tab, x) function**
   - Input: Array of numbers (tab), Number x
   - Output: Boolean indicating whether x is in the array
   
3. **add(tab, x) function**
   - Input: Array of numbers (tab), Number x
   - Output: New array with x added at the end if not already present
   
4. **remove(tab, x) function**
   - Input: Array of numbers (tab), Number x
   - Output: New array with x removed if present
   
5. **neighbors(x, y, nx, ny) function**
   - Input: Coordinates (x, y) of a cell, Size of grid (nx, ny)
   - Output: Array containing numbers of neighboring cells

6. **laby(nx, ny, dimension) procedure**
   - Input: Maze dimensions (width=nx, height=ny), Cell dimension (dimension)
   - Output: Random maze drawn in the pixel window
   
#### Apps to Use:
- **codeBoot:** Python environment for coding and testing

#### Name of Objects, Methods, and Tasks:
- **maze.py:** File name for the code
- **set_screen_mode(width, height):** App method to set pixel window resolution
- **set_pixel(x, y, color):** App method to change pixel color at coordinates (x, y)
- **export_screen():** App method to get text encoding of pixel window content

#### What is to Be Done:
- Develop functions and procedures to generate and draw mazes.
- Implement the algorithm using random numbers to create mazes.
- Use sets of numbers for horizontal and vertical walls.
- Visualize the algorithm with pixel manipulation in the codeBoot environment.
- Implement unit testing for each procedural abstraction.
- Submit the code file (maze.py) by the specified deadline.

#### Process of Doing It:
1. Implement each function as specified.
2. Use set manipulation functions to simplify the maze creation algorithm.
3. Visualize the algorithm using pixel window manipulation in codeBoot.
4. Implement unit tests for each function and procedure.
5. Ensure compliance with the specified coding standards.
6. Submit the code file through the designated Studium course website by the deadline.

### Simplified English Summary:
Create a Python code file (maze.py) with functions and procedures to generate and draw mazes using the codeBoot environment. Follow specified names and guidelines for each function and procedure. Utilize set manipulation for maze creation, visualize the algorithm using pixel manipulation, and implement unit tests. Submit the code file by the given deadline, considering accuracy, maintainability, readability, and adherence to standards for evaluation. Avoid plagiarism and external assistance.

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