first_turns = [0,12,6,13,20,1,17]
# first_turns = [0, 3, 6]

def calculate_next(num, turn, counts):
    if num in counts:
        next_num = turn - counts[num]
    else:
        next_num = 0
    counts[num] = turn
    return next_num, counts

def initialize_count(game):
    counts = {}
    for turn, num in enumerate(game):
        counts[num] = turn + 1    
    return counts

def build_game():
    pass

def find_2020th(first_turns):
    game = first_turns
    next_turn = len(game)
    count = initialize_count(game)
    print(calculate_next(0, 8, count))



print(find_2020th(first_turns))