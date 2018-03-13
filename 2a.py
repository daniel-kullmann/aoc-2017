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
        n = len(row)
        a1 = 0
        a2 = 1
        while a1 < n and a2 < n:
            v1 = row[a1]
            v2 = row[a2]
            if (v1 % v2) == 0:
                print a1, a2, v1, v2, v1/v2 
                result += v1/v2
                break
            if (v2 % v1) == 0:
                print a1, a2, v1, v2, v2/v1
                result += v2/v1
                break
            a2 += 1
            if a2 == n:
                a1 += 1
                a2 = a1+1
    return result
    
print(process(parse()))

