// https://leetcode.com/problems/longest-consecutive-sequence/

#include<iostream>
#include<vector>
#include<unordered_map>
#include<unordered_set>
#include<climits>
#include<algorithm>
using namespace std;

class Solution {
public:



	int longestConsecutive(vector<int>& nums) {
		unordered_set<int> st;
		for (int i = 0; i < (int) nums.size(); ++i)
			st.insert(nums[i]);

		int ans = 0;
		for (int val : st) {  // modern C++ iterating
			// The input has many duplicate values.
			// This is iterating on all set elements (unique)

			int len = 0;
			while(st.count(val)) {
				val += 1;
				len += 1;
			}

			ans = max(ans, len);
		}
		return ans;
	}
};

int main() {
	vector<int> nums {100,4,200,1,3,2 };
	Solution s;
	cout << s.longestConsecutive(nums);

	return 0;
}
