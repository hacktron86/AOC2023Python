def read_calibration_document(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def find_calibration_value(line):
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char

    if first_digit and last_digit:
        return int(first_digit + last_digit)
    else:
        return 0
    
def sum_calibration_values(file_name):
    lines = read_calibration_document(file_name)
    total_sum = 0

    for line in lines:
        total_sum += find_calibration_value(line)

    return total_sum

total = sum_calibration_values('input.txt')
print(total)