import random

def laby(nx, ny, dimension):
    # Initialization
    maze = [[' ' for _ in range(nx)] for _ in range(ny)]
    stack = []
    cellar = set()
    forehead = set()

    def add_to_forehead(x, y):
        # Helper function to add neighboring cells to forehead
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < nx and 0 <= ny < ny and (nx, ny) not in cellar:
                forehead.add((nx, ny))

    # Create an initial cavity
    initial_cell = (random.randint(0, ny - 1), random.randint(0, nx - 1))
    cellar.add(initial_cell)
    add_to_forehead(*initial_cell)

    # Generate Maze using Randomized Prim's Algorithm
    while cellar:
        current_cell = stack[-1] if stack else None

        if current_cell:
            x, y = current_cell
            unvisited_neighbors = [(nx, ny) for nx, ny in [(x + dx, y + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]] if 0 <= nx < nx and 0 <= ny < ny and (nx, ny) not in cellar]

            if unvisited_neighbors:
                next_cell = random.choice(unvisited_neighbors)
                stack.append(next_cell)
                maze[x][y] = 1  # Open a path between the cells
                cellar.add(next_cell)
                add_to_forehead(*next_cell)
            else:
                stack.pop()

        else:
            break

    # Print the Maze
    for row in maze:
        print(''.join(['#' if cell == 1 else ' ' for cell in row]))

# Example usage
print(laby(16, 9, 20))
