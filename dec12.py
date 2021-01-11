from dec12_input import input as directions

def calculate_final_position(directions):
    row, column = 0, 0
    facing_list = ["N", "E", "S", "W"]
    rotations = {"90": {"L": 3, "R": 1}, "270": {"L": 1, "R": 3}}
    facing_value = 1
    for direction in directions:
        order = direction["direction"]
        amount = direction["amount"]
        if order in facing_list:
            row, column = update_row_col(row, column, order, amount)
        elif order == "F":
            facing = facing_list[facing_value]
            row, column = update_row_col(row, column, facing, amount)
        else:
            if amount == 180:
                facing_value = (facing_value + 2) % 4
            else:
                facing_value = (facing_value + rotations[str(amount)][order]) % 4
    return abs(row) + abs(column)

def update_row_col(row, column, facing, amount):
    if facing == "N":
        column += amount
    elif facing == "E":
        row += amount
    elif facing == "S":
        column -= amount
    else:
        row -= amount
    return row, column


print(calculate_final_position(directions))