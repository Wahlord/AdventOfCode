#!/usr/bin/env python3

import sys
import math


def find_next_pipe(pipe, previous):
    shape = data[pipe[0]][pipe[1]]
    if shape == '|':
        if previous[0] > pipe[0]:
            return (pipe[0] - 1, pipe[1])
        else:
            return (pipe[0] + 1, pipe[1])
    if shape == '-':
        if previous[1] > pipe[1]:
            return (pipe[0], pipe[1] - 1)
        else:
            return (pipe[0], pipe[1] + 1)
    if shape == 'L':
        if previous[1] > pipe[1]:
            return (pipe[0] - 1, pipe[1])
        else:
            return (pipe[0], pipe[1] + 1)
    if shape == 'J':
        if previous[1] < pipe[1]:
            return (pipe[0] - 1, pipe[1])
        else:
            return (pipe[0], pipe[1] - 1)
    if shape == 'F':
        if previous[1] > pipe[1]:
            return (pipe[0] + 1, pipe[1])
        else:
            return (pipe[0], pipe[1] + 1)
    if shape == '7':
        if previous[1] < pipe[1]:
            return (pipe[0] + 1, pipe[1])
        else:
            return (pipe[0], pipe[1] - 1)


if __name__ == '__main__':
    data = [line.strip('\n') for line in open(sys.argv[1])]
    res1, res2 = 0, 0
    for y, line in enumerate(data):
        if line.count("S"):
            start = (y, line.index("S"))

    previous = start
    down = data[start[0] + 1][start[1]]
    up = data[start[0] - 1][start[1]]
    left = data[start[0]][start[1] - 1]
    right = data[start[0]][start[1] + 1]

    if down == 'J' or down == 'L':
        next = (start[0] + 1, start[1])
    elif up == '7' or up == 'F':
        next = (start[0] - 1, start[1])
    elif left == 'L' or left == 'F':
        next = (start[0], start[1] - 1)
    elif right == 'J' or right == '7':
        next = (start[0], start[1] + 1)

    pipe = [start, next]
    while next != start:
        current = next
        next = find_next_pipe(current, previous)
        previous = current
        pipe.append(next)

    res1 = int(math.ceil((len(pipe) - 1) / 2))

    print("Result Challenge 1: " + str(res1))

    for y in range(len(data)):
        pieces = 0
        last = ''
        for x in range(len(data[y])):
            if (y, x) not in pipe:
                if pieces % 2 == 0:
                    data[y] = data[y][:x] + 'O' + data[y][x + 1:]
                else:
                    data[y] = data[y][:x] + 'I' + data[y][x + 1:]
            elif data[y][x] == '|':
                pieces += 1
            elif data[y][x] == 'L':
                last = 'L'
            elif data[y][x] == 'F':
                last = 'F'
            elif data[y][x] == '7':
                if last == 'L':
                    pieces += 1
                last = '7'
            elif data[y][x] == 'J':
                if last == 'F':
                    pieces += 1
                last = 'J'
        res2 += data[y].count('I')

    print("Result Challenge 2: " + str(res2))
