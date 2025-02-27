with open('input.txt') as f:
    data = f.read().splitlines()

lines = [line.split() for line in data]

hand_dict = {
        'A': 1,
        'K': 2,
        'Q': 3,
        'T': 4,
        '9': 5,
        '8': 6,
        '7': 7,
        '6': 8,
        '5': 9,
        '4': 10,
        '3': 11,
        '2': 12,
        'J': 13,
        }


def rank_ties(lines):

    def sort_key(line):
        hand, number, rank = line
        card_priorities = [hand_dict.get(card, len(hand_dict) + 1)
                           for card in hand]
        return card_priorities, number, rank

    return sorted(lines, key=sort_key, reverse=True)


def rank_hand(hand, second=False, wild=0):
    wild = hand.count('J')
    if wild == 5:
        return 7
    hand = hand.replace('J', '')
    hpairs = 0
    checked_cards = []
    for card in hand:
        if card not in checked_cards:
            checked_cards.append(card)
            count = hand.count(card) + wild
            if count > hpairs:
                hpairs = count
                hcard = card
    if hpairs == 5:
        return 7
    if hpairs == 4:
        return 6
    if hpairs == 3:
        if second:
            return 3
        second_count = rank_hand(hand.replace(hcard, ''), True, wild)
        if second_count == 2:
            return 5
        return 3
    if hpairs == 2:
        if second:
            return 2
        second_count = rank_hand(hand.replace(hcard, ''), True, wild)
        if second_count == 3:
            return 5
        if second_count == 2:
            return 2
        return 1
    return 0


def old_rank_hand(hand, second=False):
    wild = hand.count('J')
    hand = hand.replace('J', '')
    for card in hand:
        count = hand.count(card) + wild
        if (count == 5):
            return 7
            break
        if (count == 4):
            return 6
            break
        if (count == 3):
            if second:
                return 3
                break
            second_count = rank_hand(hand.replace(card, ''), True)
            if (second_count == 2):
                return 5
                break
            return 3
            break
        if (count == 2):
            if second:
                return 2
                break
            second_count = rank_hand(hand.replace(card, ''), True)
            if (second_count == 3):
                return 5
                break
            if (second_count == 2):
                return 2
                break
            return 1
            break
    return 0


def sort_pairs(lines):
    sorted_lines = []
    for line in lines:
        hand, number = line
        rank = rank_hand(hand)
        sorted_lines.append([hand, number, rank])
    return sorted_lines


def sort_hands(lines):
    grouped_ranks = {}
    for line in lines:
        key = line[2]
        if key not in grouped_ranks:
            grouped_ranks[key] = []
        grouped_ranks[key].append(line)
    return grouped_ranks


ranked_hands = sort_pairs(lines)

grouped_ranks = sort_hands(ranked_hands)

for key in grouped_ranks:
    lines = grouped_ranks[key]
    grouped_ranks[key] = rank_ties(lines)


ordered_ranks = {k: grouped_ranks[k] for k in sorted(grouped_ranks)}

flatted_ranks = [(hand, num) for sublists in ordered_ranks.values()
                 for sublist in sublists
                 for hand, num, _ in [sublist] if len(hand) == 5]

sum = 0
for i in range(len(flatted_ranks)):
    hand, num = flatted_ranks[i]
    product = int(num) * (i + 1)
    sum += product

print(sum)
