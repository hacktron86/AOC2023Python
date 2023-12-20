import numpy as np

# read file strip and split
def read_file(file_path):
    trans_table = str.maketrans({'#': '2', 'O': '1', '.': '0'})
    with open(file_path) as f:
        return f.read().translate(trans_table).strip().split('\n')

# process each line of data
def create_ndarray(data):
    return [[int(x) for x in list(line)] for line in data]

# covert to np array and pad
def convert_pad_array(data):
    return np.pad(np.array(data), 1, mode='constant', constant_values=2)

# primary function processing array
def sort_sublists(array):

    # Function to sort each sublist
    def sort_sublist(sublist):
        # Count the number of 1s 
        o_count = np.sum(sublist == 1)

        # rebuilt sublist
        return np.concatenate([np.full(1, 2), 
                               np.full(o_count, 1), 
                               np.full(len(sublist) - o_count - 1, 0)])


    sorted_data = []

    for row in array:
        # Split the row on '#'
        sublists = np.split(row, np.where(row == 2)[0])
        # Remove empty arrays resulting from split
        sublists = [s for s in sublists if len(s) > 0]
        # Sort each sublist
        sorted_sublists = [sort_sublist(sublist) for sublist in sublists]
        sorted_row = np.concatenate(sorted_sublists)
        sorted_data.append(sorted_row)

    return np.array(sorted_data)


def calculate_sum_optimized(arr):
    # Create a mask for 1
    mask = arr == 1
    
    # Count 1s in each sublist
    count_1 = np.sum(mask, axis=1)
    
    # Create a vector of multipliers
    multipliers = np.arange(len(arr), 0, -1)
    
    # Multiply and sum
    total_sum = np.sum(count_1 * multipliers)
    return total_sum

# check all directions of movement
def iterate_directions(arr):
    directions = ['N', 'W', 'S', 'E']
    for direction in directions:
        if direction == 'N':
            arr = arr.T
        if direction == 'W':
            arr = arr.T
        if direction == 'S':
            arr = arr[::-1].T
        if direction == 'E':
            arr = arr[::-1].T
        arr = sort_sublists(arr)
    return arr.T[::-1].T[::-1]

# check if array already found
def check_history(arr, history):
    index = 0
    for a in history:
        if np.array_equal(arr, a):
            return index
        index += 1
    return False

# loop cycles
def cycle_arr(arr):
    prev = np.zeros_like(arr)
    cycle = 1
    history = []
    while True:
        arr = iterate_directions(arr)
        index = check_history(arr, history)
        if index:
            pattern = len(history) - index
            # why did I have to add 1 to cycle?
            mod = (1000000000 - (cycle + 1)) % pattern
            return history[-mod], cycle
        prev = arr
        history.append(prev)
        cycle += 1

data = convert_pad_array(create_ndarray(read_file('input.txt')))
directions = ['N', 'W', 'S', 'E']
sorted_data, cycle = cycle_arr(data)
sorted_data = sorted_data[1:-1, 1:-1]
print(calculate_sum_optimized(sorted_data))
