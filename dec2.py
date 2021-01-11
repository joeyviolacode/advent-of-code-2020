from dec2_input import passwords as passwords_list

def password_validator(passwords):
    count = 0
    for item in passwords:
        letter_present_count = item["password"].count(item["letter"])
        if letter_present_count >= item["low"] and letter_present_count <= item["high"]:
            count += 1
    return count

def password_validator2(passwords):
    count = 0
    for item in passwords:
        first_match = item["password"][item["low"] - 1] == item["letter"]
        second_match = item["password"][item["high"] - 1] == item["letter"]
        if first_match != second_match:
            count += 1
    return count

print(password_validator(passwords_list))
print(password_validator2(passwords_list))