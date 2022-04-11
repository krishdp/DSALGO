
// https://leetcode.com/problems/trapping-rain-water/discuss/552821/Intuitive-Javascript-Solution

/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    const size = height.length;
    const leftMax = new Array(size);
    const rightMax = new Array(size);
    let water = 0
    
    leftMax[0] = height[0]
    rightMax[size - 1] = height[size - 1];
    
    // find the height of left wall for each elevation
    for (let i = 1; i < size; i++) {
        leftMax[i] = Math.max(height[i], leftMax[i - 1]);
    }
    // find the height of right wall for each elevation
    for (let i = size - 2; i >= 0; i--) {
        rightMax[i] = Math.max(height[i], rightMax[i + 1]);
    }
    // the height of the water for each elevation would be the 
    // the height of the shorter wal minus the elevation height
    for (let i = 1; i < size - 1; i++) {
        water += Math.min(leftMax[i], rightMax[i]) - height[i]   
    }
    
    return water
};
