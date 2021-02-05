first_turns = [0,12,6,13,20,1,17]
# first_turns = [0, 3, 6]

def calculate_next(num, turn, counts):
    if num in counts.keys():
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

def build_game(game, count, final_turn):
    while len(game) < final_turn:
        next_num, count = calculate_next(game[-1], len(game), count)
        game.append(next_num)
    return game

def find_2020th(first_turns):
    game = first_turns
    count = initialize_count(game)
    game = build_game(game, count, 30000000)
    return game[-1]



print(find_2020th(first_turns))