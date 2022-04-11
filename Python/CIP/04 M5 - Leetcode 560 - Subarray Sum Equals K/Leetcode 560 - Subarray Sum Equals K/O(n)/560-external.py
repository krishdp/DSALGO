
# https://leetcode.com/problems/subarray-sum-equals-k/discuss/592003/C%2B%2BPython-solution-O(n)

def subarraySum(self, nums: List[int], k: int) -> int:
	ret = 0
	sum_freq = defaultdict(int)
	cur_sum = 0
	for num in nums:
		cur_sum += num
		if cur_sum == k:
			ret += 1
		if cur_sum - k in sum_freq:
			ret += sum_freq.get(cur_sum - k) 
		sum_freq[cur_sum] += 1
	return ret
