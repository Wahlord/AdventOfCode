#!/usr/bin/env python3

import sys
import re

if __name__ == '__main__':
    data = [line.strip('\n') for line in open(sys.argv[1])]
    # with open(sys.argv[1]) as file:
    #     data = file.read().split('\n')
    res1 = 0
    for d in data:
        nums = re.findall(r"\d", d)
        res1 += int(nums[0] + nums[-1])
    print("Result Challenge 1: " + str(res1))

    res2 = 0
    for d in data:
        d = d.replace("one", "o1e")
        d = d.replace("two", "t2o")
        d = d.replace("three", "t3e")
        d = d.replace("four", "4")
        d = d.replace("five", "5e")
        d = d.replace("six", "6")
        d = d.replace("seven", "7n")
        d = d.replace("eight", "t8e")
        d = d.replace("nine", "n9e")
        nums = re.findall(r"\d", d)
        res2 += int(nums[0] + nums[-1])
    print("Result Challenge 2: " + str(res2))
