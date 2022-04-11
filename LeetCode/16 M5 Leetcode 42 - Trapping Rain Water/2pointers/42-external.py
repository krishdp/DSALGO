# https://leetcode.com/problems/trapping-rain-water/discuss/759078/Python-solution

class Solution(object):
    def trap(self, height):
        n = len(height)
        if n < 3:
            return 0

        result, left, right = 0, 1, n-2
        left_max = height[0]
        right_max = height[n-1]

        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                result += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                result += right_max - height[right]
                right -= 1

        return result
