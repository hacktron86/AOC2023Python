import numpy as np

with open('input.txt') as f:
    lines = [line.split() for line in f.read().strip().split('\n')]
lines = np.array(lines, dtype=int)


def nextNumber(line):
    if np.sum(line) == 0:
        return 0
    diff = np.diff(line)
    return line[0] - nextNumber(diff)


result = 0
for line in lines:
    result += nextNumber(line)

print(result)
