from dec1_input import num_list
import itertools

result = [seq for seq in itertools.combinations(num_list, 3) if sum(seq) == 2020]
for item in result:
    print(item[0] * item[1] * item[2])
