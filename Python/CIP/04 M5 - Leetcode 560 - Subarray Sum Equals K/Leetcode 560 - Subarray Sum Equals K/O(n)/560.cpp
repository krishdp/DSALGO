//https://leetcode.com/problems/subarray-sum-equals-k/

#include<iostream>
#include<vector>
#include<climits>
#include<algorithm>
#include<unordered_map>
using namespace std;

class Solution {
public:

	int subarraySum(vector<int>& nums, int k) {	// O(n)
		unordered_map<int, int> prefix_table;
		prefix_table[0] = 1;	// prefix 0 always there
		int res = 0, prefix_sum = 0;

		for (int i = 0; i < (int) nums.size(); i++) {
			prefix_sum += nums[i];

			if (prefix_table.count(prefix_sum - k))
				res += prefix_table[prefix_sum - k];

			++prefix_table[prefix_sum];
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
