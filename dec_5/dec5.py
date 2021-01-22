from dec5_input import binary_list

def compute_pass_number(row, column):
    return int(row, 2) * 8 + int(column, 2)

def find_highest_pass(passes_list):
    id_list = []
    highest = 0
    for item in passes_list:
        pass_number = compute_pass_number(item["row"], item["column"])
        id_list.append(pass_number)
        if pass_number > highest:
            highest = pass_number
    return highest, id_list

highest, id_list = find_highest_pass(binary_list)

def find_seat(id_list):
    id_list.sort()
    min, max = id_list[0], id_list[-1]
    seats = list(range(min, max + 1))
    my_seat = set(seats) - set(id_list)
    print(my_seat)
    

# part 1
print(highest)

# part 2
find_seat(id_list)
