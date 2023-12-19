import numpy as np

# read file strip and split
def read_file(file_path):
    with open(file_path) as f:
        return f.read().strip().split('\n')

# process each line of data
def create_ndarray(data):
    return [list(line) for line in data]

data = np.array(create_ndarray(read_file('input.txt'))).T
data = data.T
num_columns = data.shape[1]
new_row = np.array(['#'] * num_columns)
data = np.vstack([new_row, data])
data = data.T

def sort_sublists(array):
    # Function to sort each sublist
    def sort_sublist(sublist):
        # Count the number of 'O's and '#'
        o_count = np.sum(sublist == 'O')
        hash_count = 1

        # Create a sorted array with '#' at the beginning, followed by 'O's, and then '.'
        return np.concatenate([np.full(hash_count, '#'), 
                               np.full(o_count, 'O'), 
                               np.full(len(sublist) - o_count - hash_count, '.')])


    sorted_data = []

    for row in array:
        # Split the row on '#'
        sublists = np.split(row, np.where(row == '#')[0])
        # Remove empty arrays resulting from split
        sublists = [s for s in sublists if len(s) > 0]
        # Sort each sublist
        sorted_sublists = [sort_sublist(sublist) for sublist in sublists]
        sorted_row = np.concatenate(sorted_sublists)
        sorted_data.append(sorted_row)

    return np.array(sorted_data).T

sorted_data_raw = sort_sublists(data)
sorted_data = sorted_data_raw[1:]

def calculate_sum_optimized(arr):
    # Convert to a NumPy array if it's not already one
    arr = np.array(arr)
    
    # Create a mask for 'O'
    mask = arr == 'O'
    
    # Count 'O's in each sublist
    count_O = np.sum(mask, axis=1)
    
    # Create a vector of multipliers
    multipliers = np.arange(len(arr), 0, -1)
    
    # Multiply and sum
    total_sum = np.sum(count_O * multipliers)
    return total_sum

print(calculate_sum_optimized(sorted_data))
