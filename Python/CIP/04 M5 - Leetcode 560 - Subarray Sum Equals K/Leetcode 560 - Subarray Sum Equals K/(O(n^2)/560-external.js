
// https://leetcode.com/problems/subarray-sum-equals-k/discuss/820048/JavaScript-simplest-brute-force-solution-O(N-2)

var subarraySum = function(nums, k) {
    let count = 0;
    
    for (let i = 0; i < nums.length; i++) {
        let sum = 0;
        
        for (j = i; j < nums.length; j++) {
            sum += nums[j];
            
            if (sum === k) {
                count++;
            }
        }
    }
    
    return count;
};
