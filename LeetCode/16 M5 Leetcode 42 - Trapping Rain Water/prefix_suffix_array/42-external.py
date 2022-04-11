class Solution:
    def trap(self, height: List[int]) -> int:
        s, left, right = 0, [0] * len(height), [0] * len(height)
        
        for i in range(1, len(height)):
            if height[:i] != []:
                left[i] = max(height[:i])
        
        for i in range(len(height) - 1, -1, -1):
            if height[i+1:] != []:
                right[i] = max(height[i+1:])
        
        for i in range(len(height)):
            h = min(left[i], right[i])
            if height[i] < h:
                s += h - height[i]
                
        return s
