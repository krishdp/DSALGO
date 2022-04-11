//https://leetcode.com/problems/subarray-sum-equals-k/

#include<iostream>
#include<vector>
#include<climits>
#include<algorithm>
#include<unordered_map>
using namespace std;

class Solution {
public:


	int subarraySum_v1(vector<int>& nums, int k) {	// O(n^3)
		int res = 0;

		for (int start = 0; start < (int) nums.size(); start++) {
			for (int end = start; end < (int) nums.size(); ++end) {
				int sum = 0;
				for (int idx = start; idx <= end; ++idx)
					sum += nums[idx];

				if (sum == k)
					++res;
			}
		}

		return res;
	}
};

int main() {
	vector<int> nums { 9, -9, 2, 3, 4 };
	Solution s;
	cout << s.subarraySum(nums, 9);

	return 0;
}
