import random
import numpy as np


def make_grid(width, height):
    return np.array([[random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                      for _ in range(width)]
                     for _ in range(height)])


grid = make_grid(5, 5)

pos = (1, 2)

print(grid[tuple(pos)])
