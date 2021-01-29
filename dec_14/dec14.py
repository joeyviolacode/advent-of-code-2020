from dec14_input import directions

def convert_to_bin_str(num):
    bin_str = bin(int(num))[2:]
    long_bin_str = (36 - len(bin_str)) * "0" + bin_str
    return long_bin_str

def apply_mask(bin_num, mask):
    new_bin_str = ""
    for i in range(len(mask)):
        if mask[i] != "X":
            new_bin_str += mask[i]
        else: 
            new_bin_str += bin_num[i]
    return new_bin_str

def initialize_memory(directions):
    memory = {}
    print(directions)
    for direction in directions:
        if direction["address"] == "mask":
            mask = direction["value"]
        else:
            value = convert_to_bin_str(direction["value"])
            masked_value = apply_mask(value, mask)
            memory[direction["address"]] = masked_value
    return memory

def find_sum_of_memory_values(directions):
    memory = initialize_memory(directions)
    mem_values = list(memory.values())
    mem_values_decimal = [int(num, 2) for num in mem_values]
    return sum(mem_values_decimal)

print(find_sum_of_memory_values(directions))