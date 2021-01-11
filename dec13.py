from dec13_input import arrival, schedule

#bus number - arrival % bus number
def find_bus(arrival, schedule):
    worst = max(schedule)
    best_bus = 0
    for bus in schedule:
        if bus - (arrival % bus) < worst:
            worst = bus - (arrival % bus)
            best_bus = bus
    return best_bus

def find_product(arrival, schedule):
    best_bus = find_bus(arrival, schedule)
    wait_time = best_bus - (arrival % best_bus)
    return wait_time * best_bus

print(find_product(arrival, schedule))