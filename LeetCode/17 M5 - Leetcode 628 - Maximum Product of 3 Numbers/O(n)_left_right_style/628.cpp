#include<iostream>
#include<vector>
#include<climits>
#include<algorithm>
using namespace std;

class Solution {
public:

	// mn[i]: min in range {0, i-1}
	// mx[i]: max in range {0, i-1}
	void left_min_max(vector<int>& nums, vector<int>& mn, vector<int>& mx) {
		mn = mx = nums;
		for (int i = 1; i < (int)nums.size(); ++i) {
			mn[i] = min(mn[i-1], nums[i-1]);
			mx[i] = max(mx[i-1], nums[i-1]);
		}
	}

	// mn[i]: min in range {i+1, size-1}
	// mx[i]: max in range {i+1, size-1}
	void right_min_max(vector<int>& nums, vector<int>& mn, vector<int>& mx) {
		mn = mx = nums;
		for (int i = (int)nums.size()-2; i >= 0; --i) {
			mn[i] = min(mn[i+1], nums[i+1]);
			mx[i] = max(mx[i+1], nums[i+1]);
		}
	}

	int maximumProduct(vector<int>& nums) {
		vector<int> mn_left, mx_left, mn_right, mx_right;

		left_min_max(nums, mn_left, mx_left);
		right_min_max(nums, mn_right, mx_right);

	    int max_product = INT_MIN;

	    for (int i = 1; i < (int)nums.size()-1; i++) {	// bf a position
	    	// bf the 4 possible cases
	    	max_product = max(max_product, mn_left[i] * nums[i] * mn_right[i]);
	    	max_product = max(max_product, mn_left[i] * nums[i] * mx_right[i]);
	    	max_product = max(max_product, mx_left[i] * nums[i] * mn_right[i]);
	    	max_product = max(max_product, mx_left[i] * nums[i] * mx_right[i]);
	    }

	    return max_product;
	}
};

int main() {
	Solution s;
	vector<int> nums { 5, 2, 10, 4, 17, -2, 3};
	cout<<s.maximumProduct(nums);
}

