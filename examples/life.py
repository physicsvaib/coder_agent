import numpy as np
from time import sleep

def count_neighbors(grid, i, j):
    neighbors = 0
    for x in range(max(0, i-1), min(len(grid[0]), i+2)):
        for y in range(max(0, j-1), min(len(grid[1]), j+2)):
            if (x, y) != (i, j):
                neighbors += grid[x][y]
    return neighbors

def next_generation(grid):
    new_grid = np.copy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i][j] = 0
            elif grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1
    return new_grid

def game_of_life(grid, generations=100):
    for i in range(generations):
        print(f"Generation {i+1}:")
        sleep(0.5)
        print_grid(grid)
        grid = next_generation(grid)

def print_grid(grid):
    max_length = max(len(str(i)) for row in grid for i in row) + 2
    for row in grid:
        print(" ".join(str(i).rjust(max_length) for i in row))

grid = np.array([[0,1,0],[0,0,1],[1,1,1]], dtype=int)
game_of_life(grid)