#include<iostream>
#include<vector>
#include<climits>
#include<algorithm>
using namespace std;

class Solution {
public:

	int maximumProduct(vector<int>& nums) {
	    int max_product = INT_MIN;
	    int n = nums.size();

	    for (int i = 0; i < n - 2; i++)
	        for (int j = i + 1; j < n - 1; j++)
	            for (int k = j + 1; k < n; k++)
	                max_product = max(max_product, nums[i] * nums[j] * nums[k]);

	    return max_product;
	}
};

int main() {
	Solution s;
	vector<int> nums { -20, -10, -7, -6, -5, 2, 3, 4, 5 };
	cout << s.maximumProduct(nums);
}

