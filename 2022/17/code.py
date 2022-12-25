#!/usr/bin/env python3

import sys

def setShapes():
	rock1 = [['.','.','@','@','@','@','.']]
	rock2 = [['.','.','.','@','.','.','.'],['.','.','@','@','@','.','.'],['.','.','.','@','.','.','.']]
	rock3 = [['.','.','.','.','@','.','.'],['.','.','.','.','@','.','.'],['.','.','@','@','@','.','.']]
	rock4 =  [['.','.','@','.','.','.','.'],['.','.','@','.','.','.','.'],['.','.','@','.','.','.','.'],['.','.','@','.','.','.','.']]
	rock5 = [['.','.','@','@','.','.','.'],['.','.','@','@','.','.','.']]
	rocks = [rock1, rock2, rock3, rock4, rock5]
	for rock in rocks:
		for i in range(3):
			rock.append(['.']*7)
	return rocks

def compress(arr):
	for line in range(len(arr), -1):
		noRocks = True
		for i in range(arr[line]):
			if arr[line][i] == '#' or arr[line][i] == 'x':
				noRocks = False
			elif arr[line][i] == '@':
				arr[line][i] = '#'
				noRocks = False
		if noRocks:
			arr.pop(line)

def moveDown(arr):
	positions = []
	for x in range(len(arr)):
		for y in range(7):
			if arr[x][y] == '@':
				positions.append((x,y))
	movable = True
	for pos in positions:
		if arr[pos[0]-1][pos[1]] == 'x' or arr[pos[0]-1][pos[1]] == '#':
			movable = False
	if movable:
		for pos in positions:
			arr[pos[0] - 1][pos[1]] = '@'
	return movable

def moveDir(arr, direction):
	positions = []
	for x in range(len(arr)):
		for y in range(7):
			if arr[x][y] == '@':
				positions.append((x,y))
	if direction == '<':
		move = True
		for pos in positions:
			if pos[1] == 0 or arr[pos[0]][pos[1] - 1] == '#':
				move = False
		if move:
			for pos in positions:
				arr[pos[0]][pos[1] - 1] = '@' 
	elif direction == '>':
		move = True
		for pos in positions:
			if pos[1] == 6 or arr[pos[0]][pos[1] + 1] == '#':
				move = False
		if move:
			for pos in positions:
				arr[pos[0]][pos[1] + 1] = '@' 

if __name__ == '__main__':
	directions = [line.strip('\n') for line in open(sys.argv[1])][0]
	rocks = setShapes()
	step = 0
	dirCount = 0
	state = "down"
	cave = [['x']*7]
	while step < 2022:
		rock = rocks[step % 5]
		cave = rock + cave
		falling = True
		while falling:
			if state == "down":
				falling = moveDown(cave)
				state = directions
			else:
				moveDir(cave, directions[dirCount % len(directions)])
				state = "down"
				dirCount += 1
		compress(cave)
		step += 1
		#print(step)
	res1 = str(len(cave)-1)
	print("result 1: " + res1)
	res2 = ''
	print("result 2: " + res2)

