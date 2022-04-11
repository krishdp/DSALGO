//https://leetcode.com/problems/subarray-sum-equals-k/

#include<iostream>
#include<vector>
#include<climits>
#include<algorithm>
#include<unordered_map>
using namespace std;

class Solution {
public:



	void prefix_sum(vector<int> &nums) {
		for (int i = 1; i < (int) nums.size(); ++i)
			nums[i] += nums[i - 1];	// dp[i] = A[i] + d[i-1]
	}

	int range_sum(int s, int e, vector<int> &prefix) {
		if (s == 0)
			return prefix[e];
		return prefix[e] - prefix[s - 1];
	}

	int subarraySum(vector<int>& nums, int k) {	// O(n^2)
		int res = 0;
		prefix_sum(nums);

		for (int start = 0; start < (int) nums.size(); start++)
			for (int end = start; end < (int) nums.size(); ++end)
				if (range_sum(start, end, nums) == k)
					++res;
		return res;
	}

};

int main() {
	vector<int> nums { 9, -9, 2, 3, 4 };
	Solution s;
	cout << s.subarraySum(nums, 9);

	return 0;
}
