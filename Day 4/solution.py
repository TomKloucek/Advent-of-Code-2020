import os
import sys

def split_input():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        lines = f.read()
        tests = lines.split("\n\n")
        return tests

def parse_test(pole):
    fields = []
    for i in pole:
        i = i.replace('\n', ' ').split()
        print(i)
        field = []
        for value in i:
            field.append(value.split(':')[0])
        fields.append(field)
    return fields

def valid_passports(fields):
    valid = 0
    for field in fields:
        print(field)
        if len(field) >= 7:
            if len(field) == 8:
                valid += 1
            if 'cid' not in field and len(field) == 7:
                valid += 1
    return valid




pole = split_input()

print(valid_passports(parse_test(pole)))

