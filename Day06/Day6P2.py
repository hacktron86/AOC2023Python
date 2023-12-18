from functools import reduce

with open("input.txt", 'r') as f:
    data = f.read().replace(' ', '').split('\n')

time = data[0].split(':')[1:]
distance = data[1].split(':')[1:]

races = []
for i in range(len(time)):
    races.append([int(time[i]), int(distance[i])])

record_races = []
for race in races:
    distance_dict = {i: 0 if i == 0 else ((race[0] - i) * i)
                     for i in range(0, race[0])}
    records = [x for x in distance_dict.values() if x > race[1]]
    record_races.append(records)

counts = [len(sublist) for sublist in record_races]
power = reduce(lambda acc, x: acc * x, counts, 1)
print(power)
