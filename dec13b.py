from dec13_input import schedule_spaced as schedule

test_data = [{"bus": 7, "delay": 0}, {"bus": 11, "delay": 3}, {"bus": 10, "delay": 6}]

def find_start(bus1, bus2, interval, delay):
    print("Round: " + str(bus1) + " " + str(bus2) + ", interval: " + str(interval))
    #why is this constant required?
    for i in range(bus1, bus1 * 100 * bus2, interval):
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