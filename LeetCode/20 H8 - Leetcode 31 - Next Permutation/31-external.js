// https://leetcode.com/problems/next-per  jrmutation/discuss/153271/Concise-25-lines-JavaScript-beats-100


const swap = (nums, i, j) => {
    let t = nums[i];
    nums[i] = nums[j];
    nums[j] = t;
}

const reverseSort = (nums, start, end) => {
    if (start > end) { return; }
    
    let mid = Math.floor((start + end) / 2);
    for (let i = start; i <= mid; i++) { swap(nums, i, start + end - i); }
}

const nextPermutation = (nums) => {
    if (!nums || nums.length < 2) { return; }
    
    let n = nums.length, idx = n - 1, j = n - 1;

    while (idx > 0 && nums[idx] <= nums[idx - 1]) { idx--; }
    
    if (idx === 0) { return reverseSort(nums, 0, n - 1); }
    
    while (j > idx && nums[j] <= nums[idx - 1]) { j--; }
		
    swap(nums, idx - 1, j);
    reverseSort(nums, idx, n - 1);
};
