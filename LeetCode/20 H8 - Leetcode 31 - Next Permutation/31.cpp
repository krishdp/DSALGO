// https://leetcode.com/problems/next-permutation/


#include<iostream>
#include<vector>
#include<set>
#include<unordered_map>
#include<unordered_set>
#include<climits>
#include<algorithm>
#include<cassert>
using namespace std;

class Solution {
public:
	void nextPermutation(vector<int>& nums) {
		int sz = nums.size(), i = sz - 2;
		// Find the longest non-increasing suffix subarray
		while (i >= 0 && nums[i] >= nums[i + 1])
			i--;
		if (i >= 0) {	// if not whole array
			// Get next greater element for nums[i] in the suffix
			// To handle duplicates: get the most right
			int j = sz - 1;
			while (nums[j] <= nums[i])
				j--;
			swap(nums[i], nums[j]);
		}
		// Reverse the suffix [i+1, sz-1]
		reverse(nums.begin() + i + 1, nums.end());
	}
};

int main() {
	Solution s;
	vector<int> v { 0, 1, 4, 3, 3, 2, 2, 2 };
	s.nextPermutation(v);

	for (int u = 0; u < v.size(); ++u) {
		cout << v[u] << " ";
	}

	return 0;
}
