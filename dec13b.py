from dec13_input import schedule_spaced as schedule

# calculates the start point and interval for a pair of primes or prime products such that
# bus2 - bus1 will always equal the delay when bus1 is multiplied by n * interval for any 
# positive whole number n
def find_start(bus1, bus2, interval, delay):
    print("Round: " + str(bus1) + " " + str(bus2) + ", interval: " + str(interval))
    for i in range(bus1, interval * bus2, interval):
        print("checking: " + str(i))
        if (i + delay) % bus2 == 0:
            return i, interval * bus2
    

def calculate_mods(schedule):
    bus1 = schedule[0]["bus"]
    interval = bus1
    print(schedule)
    schedule = schedule[1:]
    while len(schedule) > 0: 
        bus1, interval = find_start(bus1, schedule[0]["bus"], interval, schedule[0]["delay"])
        print("bus1: " + str(bus1))
        schedule = schedule[1:]
    return bus1


print(calculate_mods(schedule))