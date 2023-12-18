from functools import reduce

with open("input.txt", 'r') as f:
    data = [[[[number
               for number in parts.strip().split()]
              for parts in side.split("|")]
             for side in line.strip().split(":")]
            for line in f if line.strip()]

card_dict = {i: 1 for i in range(1, len(data) + 1)}

sum = 0
for line in data:
    card = int(line[0][0][1])
    for side in line[1:]:
        intersection = reduce(lambda acc, x: acc + [x]
                              if x in side[0] and x not in acc
                              else acc, side[1], [])
        filtered_intersection = [item for item in intersection if item]
        repeat = card_dict[card]
        for r in range(1, len(filtered_intersection)+1):
            card_dict[card + r] += 1 + (repeat - 1)

for key, value in card_dict.items():
    sum += value

print(sum)
