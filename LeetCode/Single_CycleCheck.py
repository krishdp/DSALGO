def hasSingleCycle(array):
	numElementsVisited = 0
	currentIndex = 0

	while numElementsVisited < len(array):
		if numElementsVisited > 0 and currentIndex == 0:
			return False
		numElementsVisited += 1
		currentIndex = getIndex(currentIndex, array)
	return currentIndex == 0

def getIndex(currentIndex, array):
	jump = array[currentIndex]
	nextIndex = (currentIndex + jump) % len(array)
	return nextIndex if nextIndex >= 0 else nextIndex + len(array)


array = [0, 1, 1, 1, 1]
print(hasSingleCycle(array))

