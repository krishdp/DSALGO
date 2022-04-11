def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1

        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeekLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeekLength)
        i = rightIdx
    return longestPeakLength


array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(array))

# Test Case 1
# {
#   "array": [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# }
# Test Case 2
# {
#   "array": []
# }
# Test Case 3
# {
#   "array": [1, 3, 2]
# }
# Test Case 4
# {
#   "array": [1, 2, 3, 4, 5, 1]
# }
# Test Case 5
# {
#   "array": [5, 4, 3, 2, 1, 2, 1]
# }
# Test Case 6
# {
#   "array": [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]
# }
# Test Case 7
# {
#   "array": [5, 4, 3, 2, 1, 2, 10, 12]
# }
# Test Case 8
# {
#   "array": [1, 2, 3, 4, 5, 6, 10, 100, 1000]
# }
# Test Case 9
# {
#   "array": [1, 2, 3, 3, 2, 1]
# }
# Test Case 10
# {
#   "array": [1, 1, 3, 2, 1]
# }
# Test Case 11
# {
#   "array": [1, 2, 3, 2, 1, 1]
# }
# Test Case 12
# {
#   "array": [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]
# }
# Test Case 13
# {
#   "array": [1, 2, 3, 3, 4, 0, 10]
# }
