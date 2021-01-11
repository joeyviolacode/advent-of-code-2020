from dec11_input import input as seats

columns = len(seats[0])
rows = len(seats)

# This doesn't need to be done on every pass.  Only once.  Need to rewrite to take this out.
#Either return neighbor array from here, or use this to return as is and put into array....
# Only once is needed.
def find_neighbors(row, column):
    neighbor_coords = [(row - 1, column - 1), (row - 1, column), (row - 1, column + 1), 
                        (row, column - 1), (row, column + 1), 
                        (row + 1, column - 1), (row + 1, column), (row + 1, column + 1)]
    neighbor_coords = [coord for coord in neighbor_coords if 
                    coord[0] >= 0 and coord[0] < rows and coord[1] >= 0 and coord[1] < columns]
    return neighbor_coords

def get_neighbor_status(neighbors, seats):
    counts = { ".": 0, "L": 0, "#": 0 }
    for neighbor in neighbors:
        counts[seats[neighbor[0]][neighbor[1]]] += 1
    return counts

def create_blank_arr():
    blank = []
    for row in range(rows):
        blank.append([])
        for column in range(columns):
            blank[row].append(0)
    return blank

def calculate_new_seating(current_seats, seat_inventory):
    new_seats = create_blank_arr()
    for row in range(rows):
        for column in range(columns):
            if current_seats[row][column] == "L":
                if seat_inventory[row][column]["#"] == 0:
                    new_seats[row][column] = "#"
                else:
                    new_seats[row][column] = "L"
            elif current_seats[row][column] == "#":
                if seat_inventory[row][column]["#"] >= 4:
                    new_seats[row][column] = "L"
                else:
                    new_seats[row][column] = "#"
            else:
                new_seats[row][column] = "."
    return new_seats

def inventory_neighbors(seats):
    seat_inventory = create_blank_arr()
    #find neighbors here
    for row in range(rows):
        for column in range(columns):
            neighbors = find_neighbors(row, column)
            #pull out here and call neighbors[r][c]
            seat_inventory[row][column] = get_neighbor_status(neighbors, seats)
    return calculate_new_seating(seats, seat_inventory)

def find_stasis(seats):
    layout_list = [seats,]
    while True:
        new_seats = inventory_neighbors(seats)
        if new_seats == seats:
            break
        layout_list.append(new_seats)
        seats = new_seats
    return layout_list

def count_seats(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == "#":
                count += 1
    return count

def calculate_answer(seats):
    final_layout = find_stasis(seats)[-1]
    return count_seats(final_layout)

print(calculate_answer(seats))

# print(find_stasis(seats)[-1])