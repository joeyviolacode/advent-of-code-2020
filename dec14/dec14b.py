from dec14_input import directions

def get_binary_list(count):
    return [bin(num)[2:].zfill(4) for num in list(range(2 ** count))]

# incomplete
def apply_mask(address, mask, bin_str):
    new_bin_str = ""
    for i in range(len(mask)):
        if mask[i] == "X":
            new_bin_str += mask[i]
        else: 
            new_bin_str += bin_num[i]
    return new_bin_str

def get_masked_list(address, mask):
    bin_list = get_binary_list(mask.count("X"))
    masked_list = []
    for bin_str in bin_list:
        masked_list.append(apply_mask(address, mask, bin_str))
    return bin_list



# print(get_masked_list("00000000000000000000000000000000X0XX", "00000000000000000000000000000000X0XX"))
print("12, 3, 14".split(", "))