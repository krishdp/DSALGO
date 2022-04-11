# src: https://www.techiedelight.com/find-triplet-maximum-product-array/


# Find a triplet having the maximum product in a list
def printTriplet(A):
 
    n = len(A)
 
    if n <= 2:        # invalid input
        print("No triplet exists. The array has less than 3 elements.")
 
    # 1. Find the index of the largest, second largest, and third largest
    # element in the list
    max_index1 = 0
    max_index2 = -1
    max_index3 = -1
 
    for i in range(1, n):
        # if the current element is less than the largest element found so far
        if A[i] > A[max_index1]:
            max_index3 = max_index2
            max_index2 = max_index1
            max_index1 = i
 
        # if the current element is less than the second largest element
        # found so far
        elif max_index2 == -1 or A[i] > A[max_index2]:
            max_index3 = max_index2
            max_index2 = i
 
        # if the current element is less than the third largest element
        # found so far
        elif max_index3 == -1 or A[i] > A[max_index3]:
            max_index3 = i
 
    # 2. Find the index of the smallest and second smallest element in the list
    min_index1 = 0
    min_index2 = -1
    for i in range(1, n):
 
        # if the current element is more than the smallest element found so far
        if A[i] < A[min_index1]:
            min_index2 = min_index1
            min_index1 = i
 
        # if the current element is more than the second smallest element
        # found so far
        elif min_index2 == -1 or A[i] < A[min_index2]:
            min_index2 = i
 
    if A[max_index1] * A[max_index2] * A[max_index3] > \
            A[min_index1] * A[min_index2] *    A[max_index1]:
        print("Triplet is", (A[max_index1], A[max_index2], A[max_index3]))
    else:
        print("Triplet is", (A[min_index1], A[min_index2], A[max_index1]))
 
 
if __name__ == '__main__':
 
    A = [-4, 1, -8, 9, 6]
    printTriplet(A)
