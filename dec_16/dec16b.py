from dec16_input import other_tickets_int
from dec16_input import rule_names, ranges_grouped, ranges_list
from dec16_input import my_ticket

def build_valid_list(ranges):
    valid_nums = []
    for _range in ranges:
        for num in range(_range[0], _range[1] + 1):
            if num not in valid_nums:
                valid_nums.append(num)
    return valid_nums

def discard_invalid_tickets(tickets, ranges_list):
    valid_list = build_valid_list(ranges_list)
    sifted_list = [ticket for ticket in tickets if all(elem in valid_list for elem in ticket)]
    return sifted_list

def get_test_ranges(range_pair):
    return ( list(range(range_pair[0][0], range_pair[0][1] + 1)) + 
             list(range(range_pair[1][0], range_pair[1][1] + 1)) )

def test_against_ranges(range_pair, num):
    return int(num >= range_pair[0][0] and num <= range_pair[0][1] + 1 or 
                num >= range_pair[1][0] and  num <= range_pair[1][1])

def build_tests(ranges_grouped):
    test_ranges = []
    for range_pair in ranges_grouped:
        test_ranges.append(get_test_ranges(range_pair))
    return test_ranges

def check_field_against_rule(range_pair, other_tickets_int, position):
    range_pair[0][0] and range_pair[0][1] + 1)) + 
             list(range(range_pair[1][0], range_pair[1][1] + 1

def find_categories():
    valid_tickets = discard_invalid_tickets(other_tickets_int, ranges_list)
    print(len(valid_tickets))

def create_empty_dict(length):
    test = dict.fromkeys(list(range(length)), 0)
    print(test)

print(build_tests(ranges_grouped))