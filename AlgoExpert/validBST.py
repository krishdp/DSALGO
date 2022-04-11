class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return validate(tree, float("-inf"), float("inf"))

def validate(tree, minimum, maximum):
	if tree is None:
		return True
	if tree.value < minimum or tree.value >= maximum:
		return False
	left = validate(tree.left, minimum, tree.value)
	right = validate(tree.right, tree.value, maximum)
	
	return left and right