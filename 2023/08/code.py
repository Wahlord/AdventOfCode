#!/usr/bin/env python3

import sys
import re
import math

if __name__ == '__main__':
    data = [line.strip('\n') for line in open(sys.argv[1])]
    res1, res2 = 0, 0
    directions = data[0]

    node_map = dict()

    for i in range(2, len(data)):
        line = re.findall(r"[A-Z]+", data[i])
        node_map[line[0]] = [line[1], line[2]]
    current_node = "AAA"
    counter = 0
    while current_node != "ZZZ":
        steps = node_map.get(current_node)
        if directions[counter % len(directions)] == 'L':
            current_node = steps[0]
        else:
            current_node = steps[1]
        counter += 1

    res1 = counter

    print("Result Challenge 1: " + str(res1))

    starting_nodes = []
    end_nodes = []
    for key in node_map.keys():
        if key[-1] == 'A':
            starting_nodes.append(key)
        if key[-1] == 'Z':
            end_nodes.append(key)
    all_finished = False
    results = []
    for i, n in enumerate(starting_nodes):
        counter = 0
        node = n
        while node[-1] != 'Z':
            steps = node_map.get(node)
            if directions[counter % len(directions)] == 'L':
                node = steps[0]
            else:
                node = steps[1]
            counter += 1
        results.append(counter)

    res2 = math.lcm(*results)

    print("Result Challenge 2: " + str(res2))
