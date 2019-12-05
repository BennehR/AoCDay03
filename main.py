activecoord = [0,0]
takencoords = []
conflictcoords = []
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

print("Tracing first wire")
for step in writeonesteps:
	handlestep(step)
print("First wire traced and coords saved")
activecoord = [0,0]
print("Active coord reset, tracing second wire")
for step in writetwosteps:
	handlestep(step)
print("Second wire traced, processing crossings")
for coords in takencoords:
	if takencoords.count(coords) > 1:
		print(f"{coords} exists more than once")
		if coords not in conflictcoords:
			conflictcoords.append(coords)
			print(f"Conflict found at {coords}")


print("Finished")