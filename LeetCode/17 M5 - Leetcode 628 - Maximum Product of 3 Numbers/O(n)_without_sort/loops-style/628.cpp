#include<iostream>
#include<vector>
#include<climits>
#include<algorithm>
using namespace std;

class Solution {
public:
	int maximumProduct(vector<int>& nums) {
		int max1 = INT_MIN, max2 = INT_MIN, max3 = INT_MIN;
		int min1 = INT_MAX, min2 = INT_MAX;

		for (int i = 0; i < (int) nums.size(); i++) {
			if (nums[i] <= min1)
				min2 = min1, min1 = nums[i];
			else if (nums[i] <= min2)
				min2 = nums[i];

			if (nums[i] >= max1)
				max3 = max2, max2 = max1, max1 = nums[i];
			else if (nums[i] >= max2)
				max3 = max2, max2 = nums[i];
			else if (nums[i] >= max3)
				max3 = nums[i];
		}
		return max(min1 * min2 * max1, max1 * max2 * max3);
	}
};

int main() {
	Solution s;
	vector<int> nums { -20, -10, -7, -6, -5, 2, 3, 4, 5 };
	cout << s.maximumProduct(nums);
}

