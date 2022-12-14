from copy import deepcopy

def processInput(path):
    with open(path) as file:
        lines = file.readlines()
    data = []
    for str in lines:
        str = str.strip("\n")
        str = str.split(" -> ")
        rocks = []
        for s in str:
            s = s.split(",")
            rocks.append((int(s[0]), int(s[1])))
        data.append(rocks)
    return data

def showMap(arr):
    for line in arr:
        str = ""
        for char in line:
            str += char
        print(str[MIN_X-10:])

def initArray(input):
    arr = []
    for i in range(MAX_Y):
        arr.append(["."]*MAX_X)
    arr.append(["x"]*MAX_X)

    for rock in input:
        for i in range(len(rock) - 1):
            cell = rock[i]
            arr[cell[1]][cell[0]] = "#"
            if rock[i][0] < rock[i + 1][0]:
                low_x = rock[i][0]
                high_x = rock[i + 1][0] + 1
            else:
                high_x = rock[i][0] + 1
                low_x = rock[i + 1][0]
            if rock[i][1] < rock[i + 1][1]:
                low_y = rock[i][1]
                high_y = rock[i + 1][1] + 1
            else:
                high_y = rock[i][1] + 1
                low_y = rock[i + 1][1]
            for x in range(low_x, high_x):
                for y in range(low_y, high_y):
                    arr[y][x] = "#"
    arr[0][500] = "+"
    return arr

def findMaxY(data):
    localMax = 0
    for line in data:
        for coord in line:
            if coord[1] > localMax: localMax = coord[1]
    return localMax + 1

def findMaxX(data):
    localMax = 0
    for line in data:
        for coord in line:
            if coord[0] > localMax: localMax = coord[0]
    return localMax + 1

def findMinX(data):
    localMin = MAX_X
    for line in data:
        for coord in line:
            if coord[0] < localMin: localMin = coord[0]
    return localMin

def fall(arr):
    current_x = 500
    current_y = 0
    while True:
        if arr[current_y + 1][current_x] == ".":
            current_y += 1
        elif arr[current_y + 1][current_x - 1] == ".":
            current_y += 1
            current_x -= 1
        elif arr[current_y + 1][current_x + 1] == ".":
            current_y += 1
            current_x += 1
        elif arr[current_y + 1][current_x] == "x":
            return True
        else:
            arr[current_y][current_x] = "o"
            return False

def iterate(arr):
    done = False
    count = 0
    while not done:
        done = fall(arr)
        count += 1
    return count - 1

DATA = processInput("input")

MAX_Y = findMaxY(DATA)
MAX_X = findMaxX(DATA)
MIN_X = findMinX(DATA)

CAVE = initArray(DATA)
CAVE_1 = deepcopy(CAVE)

showMap(CAVE)
print(iterate(CAVE))
showMap(CAVE)