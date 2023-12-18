import numpy as np

with open('input.txt') as f:
    lines = [line.split() for line in f.read().strip().split('\n')]
lines = np.array(lines, dtype=float)

result = 0
for line in lines:
    while np.sum(line) != 0:
        result += line[-1]
        line = np.diff(line)

print(result)
