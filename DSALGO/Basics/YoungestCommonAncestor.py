class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestAncestor(topAncestor, decendentOne, decendentTwo):
	depthOne = getDepth(decendentOne, topAncestor)
	depthTwo = getDepth(decendentTwo, topAncestor)

	if depthOne > depthTwo:
		return getCommonAncestor(decendentOne, decendentTwo, depthOne - depthTwo)
	else:
		return getCommonAncestor(decendentTwo, decendentOne, depthTwo - depthOne)


def getDepth(decendent, topAncestor):
	depth = 0
	while decendent != topAncestor:
		decendent = decendent.ancestor
		depth += 1
	return depth

def getCommonAncestor(lowerAncestor, upperAncestor, depth):
	while depth > 0:
		lowerAncestor = lowerAncestor.ancestor
		depth -= 1

	while lowerAncestor != upperAncestor:
		lowerAncestor = lowerAncestor.ancestor
		upperAncestor = upperAncestor.ancestor
	return lowerAncestor
