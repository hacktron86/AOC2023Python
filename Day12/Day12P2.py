from functools import cache

with open('input.txt', 'r') as f:
    data = f.read().strip()

def part2(data):

    @cache
    def dfs(sequence, groups):
        if not groups:
            return '#' not in sequence
        seq_len = len(sequence)
        group_len = groups[0]
        if seq_len - sum(groups) - len(groups) + 1 < 0:
            return 0
        has_holes = any(sequence[x] == '.' for x in range(group_len))
        if seq_len == group_len:
            return 0 if has_holes else 1
        can_use = not has_holes and (sequence[group_len] != '#')
        if sequence[0] == '#':
            return dfs(sequence[group_len+1:].lstrip('.'),
                       tuple(groups[1:])) if can_use else 0
        skip = dfs(sequence[1:].lstrip('.'), groups)
        if not can_use:
            return skip
        return skip + dfs(sequence[group_len+1:].lstrip('.'),
                          tuple(groups[1:]))

    total = 0
    for line in data.split('\n'):
        sequence, groups = line.split() 
        sequence = '?'.join([sequence] * 5)
        groups = [int(g) for g in groups.split(',')] * 5
        total += dfs(sequence, tuple(groups))

    return total


print(part2(data))

