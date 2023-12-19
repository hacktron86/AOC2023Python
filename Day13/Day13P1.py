import numpy as np

# read file strip and split into sections
def read_file(file_path):
    with open(file_path) as f:
        return f.read().strip().split('\n\n')

# split section into lines and line into sublist of characters
def process_section(section):
    return [list(line) for line in section.split()]

# process each section of data into numpy array
def create_ndarray(data):
    return [process_section(section) for section in data]

# slice array in half and compare sides
def test_reflection(arr):
    arr_len = len(arr)
    arr_mid = arr_len // 2
    return np.all(arr[0:arr_mid] == arr[arr_mid:arr_len][::-1])

# loop array slicing two smaller until empty
def find_reflection_index(arr):
    is_odd = len(arr) % 2
    arr = arr[:-1] if is_odd else arr
    while arr.shape[0] > 0:
        index = len(arr) // 2 if test_reflection(arr) else 0
        if index:
            return index
        arr = arr[:-2]
    return 0

# process picture
def process_picture(arr):
    index = 0
    index = find_reflection_index(arr)
    if len(arr) % 2 and not index:
        index = find_reflection_index(arr[::-1])
        if index:
            index = len(arr) - index
    return index

# invoke part one
def part_one(arr):
    h_indices = []
    v_indices = []
    for picture in arr:
        picture = np.array(picture)
        picture_len = len(picture)
        is_odd = picture_len % 2
        # horizontal
        index = process_picture(picture)
        if is_odd and not index:
            index = process_picture(picture[::-1])
        if index:
            h_indices.append(index)
        
        if not index:
            # vertical
            index = process_picture(picture.T)
            if is_odd and not index:
                index = process_picture(picture.T[::-1])
            if index:
                v_indices.append(index)

    return sum(v_indices) + (sum(h_indices) * 100)
        

# read in file and process
data = create_ndarray(read_file('input.txt'))

print(part_one(data))
