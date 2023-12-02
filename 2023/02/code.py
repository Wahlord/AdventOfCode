#!/usr/bin/env python3

import sys
import re

if __name__ == '__main__':
    data = [line.strip('\n').split(":") for line in open(sys.argv[1])]
    res1, res2 = 0, 0
    for d in data:
        d[0] = int(re.findall(r"\d+", d[0])[0])
        d[1] = d[1].split(";")
        game_possible = True
        r, g, b = [], [], []
        for set in d[1]:
            red = re.findall(r"\d+ red", set)
            if len(red) > 0:
                red = int(re.findall(r"\d+", red[0])[0])
            else:
                red = 0
            green = re.findall(r"\d+ green", set)
            if len(green) > 0:
                green = int(re.findall(r"\d+", green[0])[0])
            else:
                green = 0
            blue = re.findall(r"\d+ blue", set)
            if len(blue) > 0:
                blue = int(re.findall(r"\d+", blue[0])[0])
            else:
                blue = 0
            game_possible = red <= 12 and green <= 13 and blue <= 14 and game_possible
            r.append(red)
            g.append(green)
            b.append(blue)
        if game_possible:
            res1 += d[0]
        res2 += max(r) * max(g) * max(b)

    print("Result Challenge 1: " + str(res1))

    print("Result Challenge 2: " + str(res2))
