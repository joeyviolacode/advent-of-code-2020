from dec1_input import num_list as num_list

def find_product(numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                print(numbers[i] * numbers[j])


find_product(num_list)
