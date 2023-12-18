import re

with open("input.txt") as f:
    data = f.read().strip().split("\n")

data = [x.split() for x in data]


def test_string(s, target):
    test = list(map(len, filter(None, re.split(r'\.+', s))))
    return test == target

def generate_combinations(s, target, index=0):
    matches = []  # List to store matching combinations

    if index >= len(s):
        if test_string(s, target):
            matches.append(s)  # Add the matching combination to the list
        return matches

    if s[index] == '?':
        # Accumulate matches from both branches of the recursion
        matches += generate_combinations(s[:index] + '#' + s[index+1:],
                                         target, index + 1)
        matches += generate_combinations(s[:index] + '.' + s[index+1:],
                                         target, index + 1)
    else:
        # Continue recursion if the current character is not '?'
        matches += generate_combinations(s, target, index + 1)

    return matches

output = []
for line in data:
    matches = generate_combinations(line[0],
                                    list(map(int, line[1].split(","))))
    output.append(matches)

# Counting the total number of matches
total_matches = sum(len(matches) for matches in output)

print(total_matches)
