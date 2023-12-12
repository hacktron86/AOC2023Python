from functools import reduce


def process_line(data):
    powers = []
    for line in data:
        color_sums = {'red': 0, 'blue': 0, 'green': 0}
        game, sets_data = line.strip().split(':')
        sets = sets_data.split(';')
        for aset in sets:
            handfuls = [handful.strip().split()
                        for handful in aset.strip().split(',')]
            for number, color in [(int(num), col) for num, col in handfuls]:
                color_sums[color] = max(color_sums[color], number)
        powers.append(reduce(lambda x, y: x * y, color_sums.values()))
    return sum(powers)


with open('input.txt', 'r') as f:
    data = [line.strip() for line in f if line.strip()]
    total_sum = process_line(data)
    print(total_sum)
