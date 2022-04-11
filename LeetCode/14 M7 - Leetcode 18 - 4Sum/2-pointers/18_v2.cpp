// https://leetcode.com/problems/4sum/

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
	vector<vector<int>> fourSum(vector<int>& nums, int target) {
		int n = nums.size();
		sort(nums.begin(), nums.end());
		vector<vector<int> > ret;

		// Brute force 2 values: 2 pointers the remaining 2 values!
		for (int i = 0; i <= n - 4; i++) {
			if (i > 0 && nums[i] == nums[i - 1])
				continue;

			for (int j = i + 1; j <= n - 3; ++j) {
				if (j > i+1 && nums[j] == nums[j - 1])
					continue;

				int left = j + 1, right = n - 1;

				while (left < right) {	// 2-pointers
					int sum = nums[i] + nums[j] + nums[left] + nums[right] - target;

					if (!sum) {
						ret.push_back( { nums[i], nums[j], nums[left], nums[right] });
						left++;
						while (left < right && nums[left] == nums[left - 1])
							left++;
						right--;
					} else if (sum > 0)
						right--;	// let's reduce the sum
					else
						left++;		// let's increase the sum
				}
			}
		}
		return ret;
	}
};


int main() {
	vector<int> nums { 1, 0, -1, 0, -2, 2 };
	//vector<int> nums { 2,2,2,2,2 };
	Solution s;
	cout<<s.fourSum(nums, 0).size();

	return 0;
}
