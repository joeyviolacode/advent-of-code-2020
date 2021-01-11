input = """1000390
13,x,x,41,x,x,x,x,x,x,x,x,x,997,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,619,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17""".split("\n")

# input = """939
# 7,13,x,x,59,x,31,19""".split("\n")

arrival = int(input[0]) 
schedule = [int(num) for num in input[1].split(",") if num != "x"]
# print(input)
