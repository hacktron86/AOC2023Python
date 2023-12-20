def read_file(file_name):
    with open(file_name) as f:
        return f.read().strip().replace('-','').split(',')


def split_symbols(data):
    return [label.split('=') for label in data]


def get_hash(character, value):
    return ((value + ord(character)) * 17) % 256


def remove_lens(boxes, label):
    return [box for box in boxes if box[0] != label] 


def check_box(box, label):
    for lens in box:
        if lens[0] == label:
            return True
    return False


def update_lens(box, label, foc_len):
    for lens in box:
        if lens[0] == label:
            lens[1] = int(foc_len)
            return box
    raise ValueError('Label not found in box')


def iterate_boxes(data):
    boxes = {}
    for string in data:
        box_num = 0
        for chr in list(string[0]):
            box_num = get_hash(chr, box_num)
        if len(string) == 1:
            if box_num in boxes:
                if check_box(boxes[box_num], string[0]):
                    boxes[box_num] = remove_lens(boxes[box_num], string[0])
        if len(string) == 2:
            if box_num not in boxes:
                boxes[box_num] = []
            if check_box(boxes[box_num], string[0]):
                boxes[box_num] = update_lens(boxes[box_num], *string)
            else:
                boxes[box_num].append([string[0], int(string[1])])

    return boxes

# removes empty boxes
def remove_empty_boxes(boxes):
    for key in list(boxes.keys()):
        if not boxes[key]:
            boxes.pop(key)
    return boxes


def calculate_power(boxes):
    foc_powers = []
    for key in list(boxes.keys()):
        lens_count = 1
        for lens in boxes[key]:
            foc_powers.append((int(key) + 1) * lens_count * lens[1])
            lens_count += 1
    return sum(foc_powers)


data = split_symbols(read_file('input.txt'))
final_boxes = remove_empty_boxes(iterate_boxes(data))
print(calculate_power(final_boxes))
