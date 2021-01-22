from dec4_input import final_input
import re

test = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def check_passports_1(passports, list):
    count = 0
    valid_passports = []
    for item in passports:
        if item.keys() >= test:
            valid_passports.append(item)
    return valid_passports

# These three can be written as one validate_year(year, min, max), but I would
# feel like I'd need constants for all of the min and max values, so this is fine
# for now.  For production code, I would definitely use the single function
def validate_byr(byr):
    return byr >= 1920 and byr <= 2002

def validate_iyr(iyr):
    return iyr >= 2010 and iyr <= 2020

def validate_eyr(eyr):
    return eyr >= 2020 and eyr <= 2030

def validate_ecl(ecl):
    return ecl in eye_colors

def validate_hgt(hgt):
    unit = hgt[-2:]
    value = int(hgt[:-2])
    if unit == "cm":
        return value >= 150 and value <= 193
    elif unit == "in":
        return value >= 59 and value <= 76
    else:
        return False

def validate_pid(pid):
    format = re.compile("^\d{9}$")
    return format.match(pid)

def validate_hcl(hcl):
    format = re.compile("^#[0-9a-f]{6}$")
    return format.match(hcl)


def validate_passports(passports):
    valid_passports = []
    for item in passports:
        if (validate_byr(int(item["byr"])) 
            and validate_iyr(int(item["iyr"]))
            and validate_eyr(int(item["eyr"]))
            and validate_hgt(item["hgt"])
            and validate_ecl(item["ecl"])
            and validate_pid(item["pid"])
            and validate_hcl(item["hcl"])
            ):
            valid_passports.append(item)
    return valid_passports


candidate_passports = check_passports_1(final_input, test)
valid_passports = validate_passports(candidate_passports)
# for item in valid_passports:
#     print(item["pid"])


# answer to part 1
print(len(candidate_passports))
# answer to part 2
print(len(valid_passports))
