from dec9_input import input

def check_for_invalid(chunk):
    candidate = chunk[-1]
    # print(candidate)
    # print(len(chunk))
    chunk = chunk[0:25]
    # print("checking " + str(candidate) + " " + chunk[0] + " " + chunk[24] + " " + str(len(chunk)))
    for i in range(len(chunk) - 1):
        for j in range(i + 1, len(chunk)):
            # print(chunk[i] + chunk[j])
            if chunk[i] + chunk[j] == candidate:
                return True, candidate
    return False, candidate


def check_all_chunks(input):
    for i in range(len(input) - 26):
        test, candidate = check_for_invalid(input[i:i+26])
        if not test:
           return candidate


# print(check_all_chunks(input))
# print(len(input[5:31]))

# print(check_all_chunks(input))

def find_weakness(input):
    checksum = check_all_chunks(input)
    print(checksum)
    for i in range(2, len(input)):
        test = check_sections(input, i, checksum)
        if test:
            return test


def check_sections(input, length, checksum):
    for i in range(len(input) - length):
        if sum(input[i:i + length]) == checksum:
            return min(input[i:i+length]) + max(input[i:i+length])
    return None

print(find_weakness(input))

# print(sum(input[445:462]))
# print(input[445] + input[461])