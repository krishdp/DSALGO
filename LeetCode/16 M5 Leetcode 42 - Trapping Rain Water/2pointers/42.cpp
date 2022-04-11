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

	int trap(vector<int>& height) {
		int left = 0, right = height.size() - 1;
		int ans = 0;
		int left_max = 0, right_max = 0;

		while (left <= right) {	// with < fails at [5, 0, 5]
			// Compare my exact left_max with the potential right max
			if (left_max < max(right_max, height[right])) {
				left_max = max(left_max, height[left]);
				ans += left_max - height[left];
				left = left + 1;
			} else {
				right_max = max(right_max, height[right]);
				ans += right_max - height[right];
				right = right - 1;
			}
		}
		return ans;
	}

};
