from dec6_input import groups_input

def find_yesses(answer_list):
    total_yesses = 0
    for group in answer_list:
        group_yesses_set = set()
        for item in group:
            for char in item:
                group_yesses_set.add(char)
        total_yesses += len(group_yesses_set)
    return total_yesses

def find_all_yesses(answer_list):
    total_yesses = 0

    # This bit constructs the groups of sets for later comparison
    for group in answer_list:
        sets_list = []
        for item in group:
            this_set = set()
            for char in item:
                this_set.add(char)
            sets_list.append(this_set)
        result = set(sets_list[0])

        # This bit checks the intersection of all sets in each group
        for s in sets_list[1:]:
            result.intersection_update(s)
        total_yesses += len(result)
    return total_yesses

# Part one of Dec 6
print(find_yesses(groups_input))

# Part 2 of Dec 6
print(find_all_yesses(groups_input))
