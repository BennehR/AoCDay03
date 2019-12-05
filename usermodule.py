activecoord = [0,0]
takencoords = []
wireonesteps = []
wiretwosteps = []
with open("input.txt", "r") as inp:
	inputstring = inp.read()
	inputarray = inputstring.split()
	writeonesteps = inputarray[0].split(',')
	writetwosteps = inputarray[1].split(',')

def handlestep(step):
	direction = step[0]
	stepstotake = int(step[1:])
	if direction == "U":
		for x in range(0,stepstotake):
			activecoord[0] += 1
			takencoords.append(activecoord)
	elif direction == "D":
		for x in range(0,stepstotake):
			activecoord[0] -= 1
			takencoords.append(activecoord)
	elif direction == "L":
		for x in range(0,stepstotake):
			activecoord[1] -= 1
			takencoords.append(activecoord)
	elif direction == "R":
		for x in range(0,stepstotake):
			activecoord[1] += 1
			takencoords.append(activecoord)
	else:
		print("Invalid direction encountered, holding")
		input()
	print(takencoords)
	input()

for step in writeonesteps:
	handlestep(step)