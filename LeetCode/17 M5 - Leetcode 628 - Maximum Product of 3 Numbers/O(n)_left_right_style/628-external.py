# https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/

# A Python3 program to find a maximum product
# of a triplet in array of integers
import sys
 
# Function to find a maximum product of a
# triplet in array of integers of size n
def maxProduct(arr, n):
 
    # If size is less than 3, no triplet exists
    if (n < 3):
        return -1
 
    # Construct four auxiliary vectors
    # of size n and initialize them by -1
    leftMin = [-1 for i in range(n)]
    rightMin = [-1 for i in range(n)]
    leftMax = [-1 for i in range(n)]
    rightMax = [-1 for i in range(n)]
 
    # Will contain max product
    max_product = -sys.maxsize - 1
 
    # To store maximum element on
    # left of array
    max_sum = arr[0]
 
    # To store minimum element on
    # left of array
    min_sum = arr[0]
 
    # leftMax[i] will contain max element
    # on left of arr[i] excluding arr[i].
    # leftMin[i] will contain min element
    # on left of arr[i] excluding arr[i].
    for i in range(1, n):
        leftMax[i] = max_sum
         
        if (arr[i] > max_sum):
            max_sum = arr[i]
 
        leftMin[i] = min_sum
 
        if (arr[i] < min_sum):
            min_sum = arr[i]
 
    # Reset max_sum to store maximum
    # element on right of array
    max_sum = arr[n - 1]
     
    # Reset min_sum to store minimum
    # element on right of array
    min_sum = arr[n - 1]
 
    # rightMax[i] will contain max element
    # on right of arr[i] excluding arr[i].
    # rightMin[i] will contain min element
    # on right of arr[i] excluding arr[i].
    for j in range(n - 2, -1, -1):
        rightMax[j] = max_sum
         
        if (arr[j] > max_sum):
            max_sum = arr[j]
             
        rightMin[j] = min_sum
         
        if (arr[j] < min_sum):
            min_sum = arr[j]
 
    # For all array indexes i except first and
    # last, compute maximum of arr[i]*x*y where
    # x can be leftMax[i] or leftMin[i] and
    # y can be rightMax[i] or rightMin[i].
    for i in range(1, n - 1):
        max1 = max(arr[i] * leftMax[i] * rightMax[i],
                   arr[i] * leftMin[i] * rightMin[i])
        max2 = max(arr[i] * leftMax[i] * rightMin[i],
                   arr[i] * leftMin[i] * rightMax[i])
 
        max_product = max(max_product, max(max1, max2))
 
    return max_product
 
# Driver code
arr = [ 1, 4, 3, -6, -7, 0 ]
n = len(arr)
Max = maxProduct(arr, n)
 
if (Max == -1):
    print("No Triplet Exists")
else:
    print("Maximum product is", Max)
 
# This code is contributed by rag2127
