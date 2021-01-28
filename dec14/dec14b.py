from dec14_input import directions

def get_binary_list(count):
    return [bin(num)[2:].zfill(count) for num in list(range(2 ** count))]

def apply_mask(address, mask, bin_str):
    new_bin_str = ""
    for i in range(len(mask)):
        if mask[i] == "X":
            new_bin_str += bin_str[0]
            bin_str = bin_str[1:]
        elif mask[i] == "1":
            new_bin_str += "1"
        else: 
            new_bin_str += address[i]
    return new_bin_str

def get_masked_list(address, mask):
    bin_list = get_binary_list(mask.count("X"))
    masked_list = []
    for bin_str in bin_list:
        masked_list.append(apply_mask(address, mask, bin_str))
    return masked_list



print(get_masked_list("00101011", "110101XX"))
# print("12, 3, 14".split(", "))
# print(get_binary_list(1))

# print(get_binary_list("110101XX".count("X")))