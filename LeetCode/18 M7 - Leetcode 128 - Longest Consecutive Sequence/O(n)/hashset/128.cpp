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
		// Add to hashset to check if exists
		unordered_set<int> st;
		for (int i = 0; i < (int) nums.size(); ++i)
			st.insert(nums[i]);

		int ans = 0;
		for (int val : st) {  // modern C++ iterating
			if(st.count(val-1))
				continue;	// NOT sequence first element

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
