#!/usr/bin/env python3

import sys

if __name__ == '__main__':
	with open(sys.argv[1]) as file:
		data = file.read().split('\n')
	elves = []
	tmp = []
	for d in data:
		if d != '':
			tmp.append(int(d))
		else:
			elves.append(tmp)
			tmp = []

	maxCals = 0
	for e in elves:
		totalCals = 0
		for food in e:
			totalCals += int(food)
		if totalCals > maxCals : maxCals = totalCals
	res1 = str(maxCals) 
	print("result 1: " + res1)

	top3 = [0,0,0]
	for e in elves:
		total = 0
		for food in e:
			total += food
		if total > top3[0]:
			top3[2] = top3[1]
			top3[1] = top3[0]
			top3[0] = total
		elif total > top3[1]:
			top3[2] = top3[1]
			top3[1] = total
		elif total > top3[2]:
			top3[2] = total
	res2 = 0
	for f in top3: res2 += f
	print("result 2: " + str(res2))

