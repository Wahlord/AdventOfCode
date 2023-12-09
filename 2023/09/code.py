#!/usr/bin/env python3

import sys


def calc_next_value(line):
    if len(line) == 1:
        return line[0]
    next_line = []
    all_zeroes = True
    for i in range(len(line) - 1):
        next_line.append(line[i + 1] - line[i])
        all_zeroes = all_zeroes and next_line[i] == 0
    if not all_zeroes:
        next_value = calc_next_value(next_line)
        next_line.append(next_value)
    return line[-1] + next_line[-1]


def calc_first_value(line):
    if len(line) == 1:
        return [line[0]]
    next_line = []
    all_zeroes = True
    for i in range(len(line) - 1):
        next_line.append(line[i + 1] - line[i])
        all_zeroes = all_zeroes and next_line[i] == 0
    if not all_zeroes:
        first_value = calc_first_value(next_line)
        next_line = first_value + next_line
    return [line[0] - next_line[0]]


if __name__ == '__main__':
    data = [line.strip('\n') for line in open(sys.argv[1])]
    res1, res2 = 0, 0
    for i, line in enumerate(data):
        data[i] = [int(n) for n in line.split(' ')]

    for line in data:
        res1 += calc_next_value(line)
        res2 += calc_first_value(line)[0]

    print("Result Challenge 1: " + str(res1))

    print("Result Challenge 2: " + str(res2))
