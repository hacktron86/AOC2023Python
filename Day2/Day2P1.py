f = open('input.txt', 'r')
data = f.read()

# data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

data = [line for line in data.split('\n') if line.strip()]


def process_line(data):
    valid_games = []
    possible_cubes = {'red': 12, 'green': 13, 'blue': 14}

    for line in data:
        game, sets_data = line.strip().split(':')
        game = int(game.strip().split()[1])
        sets = sets_data.split(';')

        set_validation = [
                all(
                    (int(amount) <= possible_cubes[color])
                    for amount, color in (
                        handful.strip().split() for handful in aset.split(',')
                        )
                    )
                for aset in sets
                ]

        if all(set_validation):
            valid_games.append(game)

    return valid_games


valid_games = process_line(data)
sum_valid_games = sum(valid_games)
print(sum_valid_games)
