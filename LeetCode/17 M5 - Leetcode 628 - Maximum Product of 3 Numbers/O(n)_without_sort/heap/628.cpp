#include<iostream>
#include<vector>
#include<climits>
#include<algorithm>
#include<queue>
using namespace std;

class Solution {
public:

	int maximumProduct(vector<int>& nums) {
		priority_queue<int> mx_heap;	// for smallest 2 numbers
		priority_queue <int, vector<int>, greater<int>> mn_heap;

		for (int i = 0; i < (int) nums.size(); i++) {
			mx_heap.push(nums[i]);
			mn_heap.push(nums[i]);

			if(mx_heap.size() > 2)
				mx_heap.pop();

			if(mn_heap.size() > 3)
				mn_heap.pop();	// keep largest 3
		}
		// mn_heap has lowest 3 values. max3 is top
		int max1, max2, max3, min1, min2;
		max3 = mn_heap.top(), mn_heap.pop();
		max2 = mn_heap.top(), mn_heap.pop();
		max1 = mn_heap.top(), mn_heap.pop();

		min2 = mx_heap.top(), mx_heap.pop();
		min1 = mx_heap.top(), mx_heap.pop();

		return max(min1 * min2 * max1, max1 * max2 * max3);
	}

};

int main() {
	Solution s;
	vector<int> nums { -20, -10, -7, -6, -5, 2, 3, 4, 5 };
	cout << s.maximumProduct(nums);
}

