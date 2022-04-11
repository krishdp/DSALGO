def arrayOfProducts(array):
    resultArray = []
    for i in range(len(array)):
        leftSum = getProduct(array[:i])
        rightSum = getProduct(array[i+1:])
        totalSum = leftSum * rightSum
        resultArray.append(totalSum)
    return resultArray


def getProduct(array):
    total = 1
    for i in array:
        total *= i
    return total


array = [5, 1, 4, 2]
print(arrayOfProducts(array))

# Test Case 1
# {
#   "array": [5, 1, 4, 2]
# }
# Test Case 2
# {
#   "array": [1, 8, 6, 2, 4]
# }
# Test Case 3
# {
#   "array": [-5, 2, -4, 14, -6]
# }
# Test Case 4
# {
#   "array": [9, 3, 2, 1, 9, 5, 3, 2]
# }
# Test Case 5
# {
#   "array": [4, 4]
# }
# Test Case 6
# {
#   "array": [0, 0, 0, 0]
# }
# Test Case 7
# {
#   "array": [1, 1, 1, 1]
# }
# Test Case 8
# {
#   "array": [-1, -1, -1]
# }
# Test Case 9
# {
#   "array": [-1, -1, -1, -1]
# }
# Test Case 10
# {
#   "array": [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# }
# Test Case 11
# {
#   "array": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# }
