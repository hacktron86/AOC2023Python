import numpy as np


def read_lines_to_array(file_path):
    with open(file_path) as f:
        return np.array([list(line.strip()) for line in f])


def find_uniform_indices(arr, axis):
    return np.where(np.all(arr == '.', axis=axis))[0]


lines = read_lines_to_array("input.txt")

col_indices = find_uniform_indices(lines, axis=0)
row_indices = find_uniform_indices(lines, axis=1)

stars = np.where(lines == '#')

stars = np.array(list(zip(stars[0], stars[1])))


def sum_abs_diff(arr, row_indices, col_indices):
    total = 0
    duplication_factor = 999999

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            diff = np.abs(arr[i] - arr[j])
            print("first: ", arr[i], "second: ", arr[j])
            print(diff)

            row_count = np.sum((row_indices > min(arr[i][0], arr[j][0])) &
                               (row_indices < max(arr[i][0], arr[j][0])))

            col_count = np.sum((col_indices > min(arr[i][1], arr[j][1])) &
                               (col_indices < max(arr[i][1], arr[j][1])))

            print(row_count, col_count)

            diff[0] += (row_count) * duplication_factor
            diff[1] += (col_count) * duplication_factor

            total += np.sum(diff)

    return total


result = sum_abs_diff(stars, row_indices, col_indices)
print(result)
