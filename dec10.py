from dec10_input import input

input.sort()

def count_diffs(input):
    counter = [0, 1, 0, 1]
    input = input[:]
    for i in range(len(input) - 1):
        counter[input[i+1] - input[i]] += 1
    print(counter)
    return counter[3] * counter[1]

#part 1 sol
# print(count_diffs(input))

def find_threes(input):
    input.append(0)
    input.sort()
    indexes_of_3s = []
    for i in range(len(input) - 1):
        if input[i+1] - input[i] == 3:
            indexes_of_3s.append(i)
    return indexes_of_3s

def process_threes(threes_location):
    current = threes_location[0]
    threes_location = threes_location[1:]
    total = 1
    mults = [1, 1, 2, 4, 7, 13]
    while len(threes_location) > 0:
        next_num = threes_location[0]
        threes_location = threes_location[1:]
        print(next_num - current)
        total *= mults[next_num - current]
        current = next_num + 1
    return total



# print(sorted(input))
threes = find_threes(input)
threes.reverse()
threes.append(0)
threes.reverse()
print(process_threes(threes))


