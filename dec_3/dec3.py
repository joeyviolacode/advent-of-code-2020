from dec3_input import hill, width, height

slope_0 = {"x": 1, "y": 1}
slope_1 = {"x": 3, "y": 1}
slope_2 = {"x": 5, "y": 1}
slope_3 = {"x": 7, "y": 1}
slope_4 = {"x": 1, "y": 2}
slope_list = [slope_0, slope_1, slope_2, slope_3, slope_4]

def find_slope(hill_map, slope):
    x = 0
    y = 0
    tree_count = 0
    while y < height:
        if hill_map[y][x] == "#":
            tree_count += 1
        x = (x + slope["x"]) % width
        y += slope["y"]
    return tree_count

def find_many_slopes(hill_map, slopes):
    total_slopes = 1
    for slope in slopes:
        total_slopes *= find_slope(hill_map, slope)
    return total_slopes

print(find_slope(hill, slope_1))
print(find_many_slopes(hill, slope_list))

