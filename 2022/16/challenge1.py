#!/usr/bin/env python3

import sys

# find path along valves with highest flow in descending order
# if next to valve with flow higher 0 open it?
# rank und dijkstra?

# return dict with "Valve":(flow rate, [valves])
# dict wahrscheinlich doch dumm, weil keine Reihenfolge
# und nciht sortable nach flow
def parse(line):
	line = line.replace('=',';')
	line = line.split(';')
	valve = line[0][6:8]
	flow = int(line[1])
	tunnels = line[2][23:].replace(' ', '').split(',')
	data = {
		valve:[flow, tunnels, 0]
	}
	return data

if __name__ == '__main__':
	data = {}
	for line in open(sys.argv[1]):
		data.update(parse(line.strip('\n')))
	minutes = 30
	valve = "AA"
	flow = 0
	while minutes > 0:
		currentValve = data.get(valve)
		if not currentValve[2] and currentValve[0] > 0:
			flow += currentValve[0] * minutes
			data.update({valve:[currentValve[0], currentValve[1], 1]})			
			print("opening: " + valve)
		else:	
			maxFlow = -1
			for v in currentValve[1]:
				if data.get(v)[0] > maxFlow and not data.get(v)[2]:
					maxFlow = data.get(v)[0]
					valve = v
			print("moving to: " + valve)
		minutes -= 1
	res = str(flow)
	print("result: " + res)

