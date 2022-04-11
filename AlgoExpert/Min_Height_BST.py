# O(nlog(n)) | O(n)
# def minHeightBst(array):
#     return constructBST(array, None, 0, len(array)-1)


# def constructBST(array, bst, start, end):
#     if start > end:
#         return
#     mid = (start + end) // 2
#     root = array[mid]
#     if bst is None:
#         bst = BST(root)
#     else:
#         bst.insert(root)
#     constructBST(array,bst, start, mid - 1)
#     constructBST(array, bst, mid + 1, end)
#     return bst


# O(n) | O(n)
# def minHeightBst(array):
#     return constructBST(array, None, 0, len(array)-1)


# def constructBST(array, bst, start, end):
#     if start > end:
#         return
#     mid = (start + end) // 2
#     root = BST(array[mid])
#     if bst is None:
#         bst = root
#     else:
#         if array[mid] < bst.value:
#             bst.left = root
#             bst = bst.left
#         else:
#             bst.right = root
#             bst = bst.right

#     constructBST(array,bst, start, mid - 1)
#     constructBST(array, bst, mid + 1, end)
#     return bst

# O(n) | O(n)

def minHeightBst(array):
    return constructBST(array, 0, len(array)-1)


def constructBST(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = BST(array[mid])

    bst = BST(array[mid])
    
    bst.left = constructBST(array, start, mid - 1)
    bst.right = constructBST(array, mid + 1, end)
    return bst



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


array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
print(minHeightBst(array))




# Test Case 1
# {
#   "array": [1, 2, 5, 7, 10, 13, 14, 15, 22]
# }
# Test Case 2
# {
#   "array": [1]
# }
# Test Case 3
# {
#   "array": [1, 2]
# }
# Test Case 4
# {
#   "array": [1, 2, 5]
# }
# Test Case 5
# {
#   "array": [1, 2, 5, 7]
# }
# Test Case 6
# {
#   "array": [1, 2, 5, 7, 10]
# }
# Test Case 7
# {
#   "array": [1, 2, 5, 7, 10, 13]
# }
# Test Case 8
# {
#   "array": [1, 2, 5, 7, 10, 13, 14]
# }
# Test Case 9
# {
#   "array": [1, 2, 5, 7, 10, 13, 14, 15]
# }
# Test Case 10
# {
#   "array": [1, 2, 5, 7, 10, 13, 14, 15, 22]
# }
# Test Case 11
# {
#   "array": [1, 2, 5, 7, 10, 13, 14, 15, 22, 28]
# }
# Test Case 12
# {
#   "array": [1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32]
# }
# Test Case 13
# {
#   "array": [1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36]
# }
# Test Case 14
# {
#   "array": [1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36, 89]
# }
# Test Case 15
# {
#   "array": [1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36, 89, 92]
# }
# Test Case 16
# {
#   "array": [1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36, 89, 92, 9000]
# }
# Test Case 17
# {
#   "array": [1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36, 89, 92, 9000, 9001]
# }