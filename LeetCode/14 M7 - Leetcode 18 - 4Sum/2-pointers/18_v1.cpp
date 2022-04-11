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
		set<vector<int> > filter;

		// Brute force 2 values: 2 pointers the remaining 2 values!
		for (int i = 0; i <= n - 4; i++) {
			for (int j = i + 1; j <= n - 3; ++j) {
				int left = j + 1, right = n - 1;

				while (left < right) {	// 2-pointers
					int sum = nums[i] + nums[j] + nums[left] + nums[right] - target;

					if (!sum) {
						vector<int> v { nums[i], nums[j], nums[left], nums[right] };
						sort(v.begin(), v.end());
						if(filter.insert(v).second)
							ret.push_back(v);
						left++, right--;
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
	vector<int> nums { 0, 0, 0, 0};
	//vector<int> nums { 2,2,2,2,2 };
	Solution s;
	cout<<s.fourSum(nums, 0).size();

	return 0;
}
