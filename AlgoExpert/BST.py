# Recursive Solution's
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
		if value < self.value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)
		return self

    def contains(self, value):
        # Write your code here.
        if value < self.value:
			if self.left is None:
				return False
			else:
				return self.left.contains(value)
		elif value > self.value:
			if self.right is None:
				return False
			else:
				return self.right.contains(value)
		else:
			return True
			

    def remove(self, value, parent=None):
		if value < self.value:
			if self.left is not None:
				self.left.remove(value, self)
		elif value > self.value:
			if self.right is not None:
				self.right.remove(value, self)
		else:
			if self.left is not None and self.right is not None:
				self.value = self.right.getMinValue()
				self.right.remove(self.value, self)
			elif parent is None:
				if self.left is not None:
					self.value = self.left.value
					self.right = self.left.right
					self.left = self.left.left
				elif self.right is not None:
					self.value = self.right.value
					self.left = self.right.left
					self.right = self.right.right
				else:
					pass
			elif parent.left == self:
				if self.left is not None:
					parent.left = self.left
				else:
					parent.left = self.right
			elif parent.right == self:
				if self.left is not None:
					parent.right = self.left
				else: 
					parent.right = self.right
		return self
	
	def getMinValue(self):
		if self.left is None:
			return self.value
		else:
			return self.left.getMinValue()


# Iterative Solution
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
		currentNode = self
		while True:
			if value < currentNode.value:
				if currentNode.left is None:
					currentNode.left = BST(value)
					break
				else:
					currentNode = currentNode.left
			else:
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else:
					currentNode = currentNode.right
		return self		

    def contains(self, value):
        currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
				currentNode = currentNode.left
			elif value > currentNode.value:
				currentNode = currentNode.right
			else:
				return True
		return False

    def remove(self, value, parentNode = None):
		currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.left
			elif value > currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.right
			else:
				if currentNode.left is not None and currentNode.right is not None:
					currentNode.value = currentNode.right.getMinValue()
					currentNode.right.remove(currentNode.value, currentNode)
				elif parentNode is None:
					if currentNode.left is not None:
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						currentNode.left = currentNode.left.left
					elif currentNode.right is not None:
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right
					else:
						pass
				elif parentNode.left == currentNode:
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
				elif parentNode.right == currentNode:
					parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
				break
		return self
	
	def getMinValue(self):
		currentNode = self
		while currentNode.left is not None:
			currentNode = currentNode.left
		return currentNode.value


# {
#   "rootValue": 10,
#   "classMethodsToCall": [
#     {
#       "arguments": [5],
#       "method": "insert"
#     },
#     {
#       "arguments": [15],
#       "method": "insert"
#     },
#     {
#       "arguments": [2],
#       "method": "insert"
#     },
#     {
#       "arguments": [5],
#       "method": "insert"
#     },
#     {
#       "arguments": [13],
#       "method": "insert"
#     },
#     {
#       "arguments": [22],
#       "method": "insert"
#     },
#     {
#       "arguments": [1],
#       "method": "insert"
#     },
#     {
#       "arguments": [14],
#       "method": "insert"
#     },
#     {
#       "arguments": [12],
#       "method": "insert"
#     },
#     {
#       "arguments": [10],
#       "method": "remove"
#     },
#     {
#       "arguments": [15],
#       "method": "contains"
#     }
#   ]
# }