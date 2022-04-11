# src: https://leetcode.com/problems/maximum-product-of-three-numbers/solution/304829

import heapq

class Solution:
    def maximumProduct(self, array):
        largest = heapq.nlargest(3, array)
        smallest = heapq.nsmallest(2,array)

        return max(largest[0] * largest[1] * largest[2], largest[0] * smallest[0] * smallest[1] )


# nlargest is O(n log k) for selecting k elements: the most efficient way
# as k is either 2 or 3, this is O(n)
# https://github.com/python/cpython/blob/2.7/Lib/heapq.py#L203


