from dec16_input import ranges_list as ranges
from dec16_input import other_tickets_int

def build_valid_list(ranges):
    valid_nums = []
    for _range in ranges:
        for num in range(_range[0], _range[1] + 1):
            if num not in valid_nums:
                valid_nums.append(num)
    return valid_nums

def find_exceptions_total(ranges):
    valid_list = build_valid_list(ranges)
    exceptions = []
    

print(build_valid_list(ranges))