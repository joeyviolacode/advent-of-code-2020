input = """1000390
13,x,x,41,x,x,x,x,x,x,x,x,x,997,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,619,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17""".split("\n")

# various test inputs

# input = """129080918
# 1789,37,47,1889""".split("\n")
# input = """939
# 7,13,x,x,59,x,31,19""".split("\n")

arrival = int(input[0]) 
schedule = [int(num) for num in input[1].split(",") if num != "x"]
schedule_spaced = input[1].split(",")
schedule_spaced = [{"bus": int(bus), "delay": index} for index, bus in enumerate(schedule_spaced) if bus != "x"]

# print(input)
