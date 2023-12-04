#!/usr/bin/env python3

import sys
import re

if __name__ == '__main__':
    data = [line.strip('\n').split(":") for line in open(sys.argv[1])]
    res1, res2 = 0, 0
    winning_numbers = []
    numbers = []
    for d in data:
        d[0] = int(re.findall(r"\d+", d[0])[0])
        d[1] = d[1].split("|")
        winning_numbers.append(re.findall(r"\d+", d[1][0]))
        numbers.append(re.findall(r"\d+", d[1][1]))

    for card in range(len(data)):
        matches = 0
        for num in winning_numbers[card]:
            if num in numbers[card]:
                matches += 1
        if matches > 0:
            res1 += 2 ** (matches - 1)

    print("Result Challenge 1: " + str(res1))

    copies = []
    for d in data:
        copies.append(1)

    for card in range(len(data)):
        matches = 0
        for num in winning_numbers[card]:
            if num in numbers[card]:
                matches += 1
        for m in range(matches):
            copies[card + m + 1] += copies[card]

    for c in copies:
        res2 += c

    print("Result Challenge 2: " + str(res2))
