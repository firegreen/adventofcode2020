from passport_processing_input import input
import re

required = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
passports = input.split('\n\n')
result = 0
for passport in passports:
    entries = passport.replace('\n', ' ').split(' ')
    entries = dict((entry.split(':') for entry in entries))
    if any((key not in entries for key in required)):
        continue

    try:
        byr = int(entries["byr"])
        if byr < 1920 or byr > 2002:
            continue
        iyr = int(entries["iyr"])
        if iyr < 2010 or iyr > 2020:
            continue
        eyr = int(entries["eyr"])
        if eyr < 2020 or eyr > 2030:
            continue
        height = entries["hgt"]
        height_value = int(height[:-2])
        if height.endswith("cm"):
            if height_value<150 or height_value>193:
                continue
        elif height.endswith("in"):
            if height_value<59 or height_value>76:
                continue
        else:
            continue

        if not re.match(r"#[0-9a-f]", entries["hcl"]):
            continue
        if entries["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            continue
        pid = int(entries["pid"])
        if len(entries["pid"]) != 9:
            continue
    except ValueError as e:
        print(e)
    else:
        result += 1

print(len(passports), result)
