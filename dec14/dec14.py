from dec14_input import directions

def convert_to_bin_str(num):
    bin_str = bin(num)[2:]
    long_bin_str = (36 - len(bin_str)) * "0" + bin_str
    print(long_bin_str)

convert_to_bin_str(32)