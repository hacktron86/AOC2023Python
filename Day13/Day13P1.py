import numpy as np

with open('input.txt') as f:
    data = [section.split() for section in f.read().strip().split('\n\n')]

data = [[np.array(x, dtype=str) for x in section] for section in data]

for i in data:
    print(i)
    print()
    print()
