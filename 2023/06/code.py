#!/usr/bin/env python3

import sys
import re

if __name__ == '__main__':
    data = [line.strip('\n') for line in open(sys.argv[1])]
    res1, res2 = 1, 0
    times = [int(t) for t in re.findall(r"\d+", data[0])]
    distances = [int(d) for d in re.findall(r"\d+", data[1])]
    races = range(0, len(times))

    for race in races:
        wins = 0
        for t in range(times[race]):
            if t * (times[race] - t) > distances[race]:
                wins += 1
        res1 *= wins

    print("Result Challenge 1: " + str(res1))

    time = int("".join(re.findall(r"\d+", data[0])))
    distance = int("".join(re.findall(r"\d+", data[1])))
    min_time = 0
    while min_time * (time - min_time) < distance:
        min_time += 1

    res2 = time - min_time * 2 + 1 #+1 for reasons

    print("Result Challenge 2: " + str(res2))
