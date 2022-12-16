#!/usr/bin/env python3

import sys

def parse(line):
	return (line[0], line[-1])

if __name__ == '__main__':
	data = [parse(line.strip('\n')) for line in open(sys.argv[1])]
	
	score = 0
	for game in data:
		if game[1] == 'X':
			score += 1
			if game[0] == 'C': score += 6
			if game[0] == 'A': score += 3
		elif game[1] == 'Y':
			score += 2
			if game[0] == 'A': score += 6
			if game[0] == 'B': score += 3
		elif game[1] == 'Z':
			score += 3
			if game[0] == 'B': score += 6
			if game[0] == 'C': score += 3
	res1 = str(score)
	print("result1: " + res1)	

	score = 0		
	for game in data:
		if game[1] == 'X':
			if game[0] == 'A': score += 3
			if game[0] == 'B': score += 1
			if game[0] == 'C': score += 2
		elif game[1] == 'Y':
			score += 3 
			if game[0] == 'A': score += 1
			if game[0] == 'B': score += 2
			if game[0] == 'C': score += 3
		elif game[1] == 'Z':
			score += 6
			if game[0] == 'A': score += 2
			if game[0] == 'B': score += 3
			if game[0] == 'C': score += 1
	res2 = str(score)
	print("result2: " + res2)

