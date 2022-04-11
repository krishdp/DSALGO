
# https://leetcode.com/problems/subarray-sum-equals-k/discuss/102144/TLE-for-cumulative-sum-in-python
# Time Limit Exceeded	

class Solution(object):
    def subarraySum(self, nums, k):
        if not nums:
            return 0
        count = 0
        nLen = len(nums)
        for i in range(nLen):
            last = 0
            for j in range(i, nLen):
                last = last + nums[j]
                if last == k:
                    count += 1
        return count
