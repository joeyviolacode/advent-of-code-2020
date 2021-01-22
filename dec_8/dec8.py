from dec8_input import input_tuples as input


# def find_repeat(code):
#     index = 0
#     acc = 0
#     list_of_indices = []
#     while not code[index][2]:
#         print("Hit while")
#         print("Running line " + str(index) + ": " + code[index][0] + ", " + code[index][1] + ", " + str(code[index][2]))
#         code[index][2] = True
#         list_of_indices.append(index)
#         if code[index][0] == "jmp":
#             index = index + int(code[index][1])
#         elif code[index][0] == "acc":
#             acc = acc + int(code[index][1])
#             index += 1
#         else:
#             index += 1
#     return acc, list_of_indices


# # candidates = find_repeat(input)
# # print(candidates[1])
# acc, length = find_repeat(input)
# print(len(length))
# print(acc)


# def run_from_index(code, start_index):
#     index = start_index
#     acc = 0
#     while not code[index][2] == True:
#         code[index][2] = True
#         if code[index][0] == "nop":
#             index = index + int(code[index][1])
#         elif code[index][0] == "acc":
#             acc = acc + int(code[index][1])
#             index += 1
#         else:
#             index += 1
#         if index == len(code) - 1:
#             return start_index
#     return None

# def check_starts(code):
#     for i in range(len(code)):
#         result = run_from_index(code, i)
#         if result is not None:
#             return result

def run_with_change(old_code, change_index):
    code = [[item[0], item[1], item[2]] for item in old_code]
    if code[change_index][0] == "nop":
        code[change_index][0] = "jmp"
        #print("changed")
    elif code[change_index][0] == "jmp":
        code[change_index][0] = "nop"
        #print("changed")
    index = 0
    acc = 0
    #print("testing index: " + str(change_index))
    while not code[index][2]:
        #print("Hit while!!! " + str(index))
        #print("Running line " + str(index) + ": " + code[index][0] + ", " + code[index][1] + ", " + str(code[index][2]))
        code[index][2] = True
        if code[index][0] == "jmp":
            index = index + int(code[index][1])
        elif code[index][0] == "acc":
            acc = acc + int(code[index][1])
            index += 1
        else:
            index += 1
        if index == (len(code) - 1):
            print("Made it!")
            return acc


def run_all_with_change(code):
    for index in range(180, 190):
        new_code = [item for item in code]       
        test = print(run_with_change(new_code, index))
        if test is not None:
            return test

print(run_all_with_change(input))

# def run_change_188(input):
#     print(run_with_change(input, 188))


# def run_from_start(code, start_index):
#     # if code[change_index][0] == "nop":
#     #     code[change_index][0] = "jmp"
#     # elif code[change_index][0] == "jmp":
#     #     code[change_index][0] = "nop"
#     index = start_index
#     acc = 0
#     while not code[index][2]:
#         print("Running line " + str(index) + ": " + code[index][0] + ", " + code[index][1] + ", " + str(code[index][2]))
#         code[index][2] = True
#         if code[index][0] == "jmp":
#             index = index + int(code[index][1])
#         elif code[index][0] == "acc":
#             acc = acc + int(code[index][1])
#             index += 1
#         else:
#             index += 1
#         if index == len(code) - 1:
#             print("Made it!")
#             return start_index
#     return None

# # print(run_from_start(input, 646))
# # print(check_starts(input))

# def count_nop_jmp(code):
#     nops = 0
#     jmps = 0
#     for item in code:
#         if item[0] == "jmp":
#             jmps += 1
#         if item[0] == "nop":
#             nops += 1
#     return jmps, nops

# # jmps, nops = count_nop_jmp(input)
# # print(str(jmps))
# # print(str(nops))

# # print(find_repeat(input))

# # def find_change(code):
# #     for i in range(len(code)):
# #         if code[i][0] == "nop" and i + int(code[i][1]) >= 646:
# #             return i

# # print(find_change(input))