def read_file(file_name):
    with open(file_name) as f:
        return f.read().strip().split(',')

data = read_file('input.txt')

values = []
for string in data:
    value = 0
    for chr in list(string):
        value = ((value + ord(chr)) * 17) % 256
    values.append(value)

print(values)
print(sum(values))
