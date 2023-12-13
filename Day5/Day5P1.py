with open('input.txt', 'r') as file:
    seeds, data = file.read().strip().split('\n', 1)

data = data.strip().split('\n\n')

processed_data = []

seeds = seeds.split(':')[1].split()

for section in data:
    processed_section = []
    title, *number_lines = section.split('\n')

    for line in number_lines:
        numbers = [num for num in line.split()]
        processed_section.append(numbers)

    processed_data.append(processed_section)

processed_seeds = []
for seed in seeds:
    new_seed = int(seed)
    for map in processed_data:
        for line in map:
            dst, st, length = int(line[0]), int(line[1]), int(line[2])
            if new_seed in range(st, st + length):
                new_seed = new_seed - st + dst
                break
    processed_seeds.append(new_seed)

print(min(processed_seeds))
