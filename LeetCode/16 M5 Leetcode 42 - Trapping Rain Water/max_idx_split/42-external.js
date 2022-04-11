
// https://leetcode.com/problems/trapping-rain-water/discuss/1303392/JavaScript-or-O(n)-or-96.09

var trap = function(height) {
    if (height.length === 0) return 0;
    let maxIndex = findMaxIndex(height);
    let ans = 0;
    let left_max = height[0];
    for (let i = 1; i < maxIndex; i++) { // from 0 to maxIndex
        if (height[i] < left_max) ans += left_max - height[i];
        if (height[i] > left_max) left_max = height[i];
    }
    let rigth_max = height[height.length - 1]
    for (let i = height.length - 2; i > maxIndex; i--) { // from length - 1 to maxIndex
        if (height[i] < rigth_max) ans += rigth_max - height[i];
        if (height[i] > rigth_max) rigth_max = height[i];
    }
    
    return ans
};

function findMaxIndex(arr) { // find index of max value
    let maxIndex = 0;
    let maxItem = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > maxItem) maxItem = arr[i], maxIndex = i;
    }
    return maxIndex;
}
