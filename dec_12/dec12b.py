from dec12_input import input as directions

# Haven't thought about this too much, but there are a lot of params being passed around.  Maybe better to
# use a single dict that keeps everything?  Or just break it up more?  Three dicts would work, one for ship,
# one for waypoint, and one for the input pair

def calculate_final_position(directions):
    ship_ew, ship_ns = 0, 0
    waypoint_ew, waypoint_ns = 10, 1
    for direction in directions:
        order = direction["direction"]
        amount = direction["amount"]
        if order in ["N", "E", "S", "W"]:
            waypoint_ew, waypoint_ns = update_waypoint(waypoint_ew, waypoint_ns, order, amount)
        elif order == "F":
            ship_ew, ship_ns, waypoint_ew, waypoint_ns = update_ship(ship_ew, ship_ns, waypoint_ew, waypoint_ns, amount)
        else:
            waypoint_ew, waypoint_ns = rotate_waypoint(ship_ew, ship_ns, waypoint_ew, waypoint_ns, order, amount)
    return abs(ship_ew) + abs(ship_ns)

def update_waypoint(waypoint_ew, waypoint_ns, direction, amount):
    if direction == "N":
        waypoint_ns += amount
    elif direction == "E":
        waypoint_ew += amount
    elif direction == "S":
        waypoint_ns -= amount
    else:
        waypoint_ew -= amount
    return waypoint_ew, waypoint_ns

def update_ship(ship_ew, ship_ns, waypoint_ew, waypoint_ns, amount):
    ew_delta = waypoint_ew - ship_ew
    ns_delta = waypoint_ns - ship_ns
    ship_ew += (ew_delta * amount)
    ship_ns += (ns_delta * amount)
    waypoint_ew = ship_ew + ew_delta
    waypoint_ns = ship_ns + ns_delta
    return ship_ew, ship_ns, waypoint_ew, waypoint_ns

def rotate_waypoint(ship_ew, ship_ns, waypoint_ew, waypoint_ns, direction, amount):
    #indicates clockwise rotation in units of 90 degrees
    rotations = {"90": {"L": 3, "R": 1}, "180": {"L": 2, "R": 2}, "270": {"L": 1, "R": 3}}
    this_rotation = rotations[str(amount)][direction]
    ew_delta = waypoint_ew - ship_ew
    ns_delta = waypoint_ns - ship_ns
    if this_rotation == 1:
        ew_delta, ns_delta = ns_delta, -ew_delta
    elif this_rotation == 2:
        ew_delta, ns_delta = -ew_delta, -ns_delta
    else:
        ew_delta, ns_delta = -ns_delta, ew_delta
    return ship_ew + ew_delta, ship_ns + ns_delta



print(calculate_final_position(directions))