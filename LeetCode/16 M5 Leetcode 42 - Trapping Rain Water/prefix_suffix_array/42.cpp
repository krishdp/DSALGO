// https://leetcode.com/problems/trapping-rain-water/

#include<iostream>
#include<vector>
#include<unordered_map>
#include<unordered_set>
#include<climits>
#include<algorithm>
using namespace std;

class Solution {
public:
	// mx[i]: max in range {0, i}
	void left_max(vector<int>& nums, vector<int>& mx) {
		mx = nums;
		for (int i = 1; i < (int) nums.size(); ++i)
			mx[i] = max(mx[i - 1], nums[i]);
	}

	// mx[i]: max in range {i, size-1}
	void right_max(vector<int>& nums, vector<int>& mx) {
		mx = nums;
		for (int i = (int) nums.size() - 2; i >= 0; --i)
			mx[i] = max(mx[i + 1], nums[i]);
	}

	int trap(vector<int> heights) {
		int n = heights.size();
		if (n <= 2)
			return 0;

		vector<int> left_mx, right_mx;
		left_max(heights, left_mx);
		right_max(heights, right_mx);

		int traped = 0;
		for (int i = 0; i < n; i++)
			traped += min(left_mx[i], right_mx[i]) - heights[i];

		return traped;
	}
};

int main() {
	vector<int> nums { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
	Solution s;
	cout<<s.trap(nums);

	return 0;
}
