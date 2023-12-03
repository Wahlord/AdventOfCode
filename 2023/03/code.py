#!/usr/bin/env python3

import sys
import re

if __name__ == '__main__':
    data = [line.strip('\n') for line in open(sys.argv[1])]
    res1, res2 = 0, 0

    # find all numbers per line
    # store location
    # serach for symbols
    nums = []
    positions = []
    for line in data:
        cnums = re.findall(r"\d+", line)
        nums.append(cnums)
        pos = []
        if len(cnums) > 0:
            for num in cnums:
                # print(num)
                # res2 += int(num)
                pos.append(line.find(num))
        positions.append(pos)
    # print(nums)
    # print(positions)

    for i in range(len(data)):
        for j, n in enumerate(nums[i]):
            length = len(n)
            # print(n, length)
            # res2 += int(nums[i][n])
            match = False
            for x in range(max(positions[i][j] - 1, 0), min(positions[i][j] + length + 1, len(data[0]))):
                # if x < 0: continue
                for y in range(max(i - 1, 0), min(i + 2, len(data))):
                    # if y < 0: continue
                    # if y == len(data): break
                    # elif x == len(data[y]): break
                    match = match or (data[y][x] not in ['0', '1', '2', '3', '4', '5', '6', '7' ,'8', '9', '.'])
            if match:
                # print(nums[i][n])
                res1 += int(n)

    print("Result Challenge 1: " + str(res1)) # is of by 88 and missing 6 numbers...

    print("Result Challenge 2: " + str(res2))
