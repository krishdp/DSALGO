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

		int ans = 0;
		int max_idx = 0;	// max index block the 2 sides
		for (int i = 1; i < (int) height.size(); i++)
			if (height[max_idx] < height[i])
				max_idx = i;

		int left_max = 0;
		for (int i = 0; i < max_idx; i++) {
			left_max = max(left_max, height[i]);
			ans += left_max - height[i];
		}

		int right_max = 0;
		for (int i = (int) height.size() - 1; i > max_idx; i--) {
			right_max = max(right_max, height[i]);
			ans += right_max - height[i];
		}


		return ans;


	}
};

int main() {
	vector<int> nums { 5, 2, 7, 3, 5, 7, 1, 5 };
	//vector<int> nums { 10, 2, 5 };
	Solution s;
	cout << s.trap(nums);

	return 0;
}
