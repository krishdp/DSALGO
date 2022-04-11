r
// https://leetcode.com/problems/trapping-rain-water/discuss/312091/Javascript-2-pointer

/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    if (height.length === 0) return 0;
    
    let i = 0;
    let j = height.length-1;
    
    let leftMax = 0;
    let rightMax = 0;
    let result = 0;
    
    while(i<=j){
        if (rightMax > leftMax){
            if (height[i] > leftMax) leftMax = height[i];
            else result += leftMax-height[i];
            i++;
        }else{
            if (height[j] > rightMax) rightMax = height[j];
            else result += rightMax-height[j];
            j--;
        }
    }
    return result;
};
