
// https://leetcode.com/problems/subarray-sum-equals-k/discuss/1138185/JavaScript-Hashmap

const subarraySum = (nums, k) => {
    const hashmap = {0: 1}
    let count = 0, total = 0
    for(const num of nums) {
        total += num
        if(hashmap[total - k]) count += hashmap[total - k]
        hashmap[total] ? hashmap[total]++ : hashmap[total] = 1
    }
    return count
};
