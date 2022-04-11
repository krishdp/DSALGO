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

// I did not explain this way. No need to burn time

class Solution {
public:
	vector<vector<int>> fourSum(vector<int>& nums, int target) {
		int n = nums.size();
		unordered_map<int, vector<int>> table;	// let's encode every pair as an int (think 2d array flattening)
		table.reserve(n * n);

		for (int i = 0; i < n; ++i) {
			for (int j = i + 1; j < n; ++j) {
				int sum = nums[i] + nums[j];
				table[sum].push_back(i * n + j);
			}
		}
		vector<vector<int>> ret;
		set<vector<int>> result;

		for (int k = 0; k < n; ++k) {
			for (int l = k + 1; l < n; ++l) {
				int sum = target - (nums[k] + nums[l]);
				if (!table.count(sum))
					continue;

				for (int &cell : table[sum]) {
					int i = cell / n, j = cell % n;
					if (i == k || i == l || j == k || j == l)
						continue;

					vector<int> v { nums[i], nums[j], nums[k], nums[l] };
					sort(v.begin(), v.end());
					if(result.insert(v).second)
						ret.push_back(v);
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
	s.fourSum(nums, 0);

	return 0;
}
