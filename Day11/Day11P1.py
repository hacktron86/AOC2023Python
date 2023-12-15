import numpy as np


def read_lines_to_array(file_path):
    with open(file_path) as f:
        return np.array([list(line.strip()) for line in f])


def find_uniform_indices(arr, axis):
    return np.where(np.all(arr == '.', axis=axis))[0]


def duplicate_elements(arr, indices, axis):
    for index in sorted(indices, reverse=True):
        if axis == 0:
            arr = np.insert(arr, index, arr[index], axis=0)
        elif axis == 1:
            arr = np.insert(arr, index, arr[:, index], axis=1)
    return arr


lines = read_lines_to_array("input.txt")

col_indices = find_uniform_indices(lines, axis=0)
row_indices = find_uniform_indices(lines, axis=1)

lines = duplicate_elements(lines, row_indices, axis=0)
lines = duplicate_elements(lines, col_indices, axis=1)

stars = np.where(lines == '#')

stars = np.array(list(zip(stars[0], stars[1])))


def sum_abs_diff(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            difference = np.sum(np.abs(arr[i] - arr[j]))
            total += difference
    return total


result = sum_abs_diff(stars)
print(result)
