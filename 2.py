#!/usr/bin/env python


def parse():
    result = []
    f = open("2.input")
    for line in f.readlines():
        line.strip()
        if line != "":
            result.append([int(k) for k in line.split("\t") if k != ''])
    return result

def process(input):
    result = 0
    for row in input:
        minValue = min(row)
        maxValue = max(row)
        print minValue, maxValue, row
        result += maxValue - minValue
    return result
print(process(parse()))

