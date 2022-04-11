// https://leetcode.com/problems/4sum/discuss/1341602/Python-or-Javascript-or-HashMap


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    
    let hashMap = {};
    let output = [];
    let uniqueMap = {};
    
    for (let i = 0; i < nums.length; i++){
        for (let j = i+1; j < nums.length; j++){
            
            if (hashMap[nums[i]+nums[j]] ){
                hashMap[nums[i]+nums[j]].push([i, j, nums[i], nums[j]]);
            } else {
                hashMap[nums[i]+nums[j]] = [[i, j, nums[i], nums[j]]];
            }
        }
    }
    for (let i = 0; i < nums.length; i++){
        for (let j = i+1; j < nums.length; j++){
            let complement = target - (nums[i]+nums[j]);
            
            if(hashMap[complement]){
                // Now I went to see if
                for (let k = 0; k < hashMap[complement].length; k++){
                    
                    if (i !=  hashMap[complement][k][0] && i != hashMap[complement][k][1] && j != hashMap[complement][k][0] && j != hashMap[complement][k][1]){
                        
                        temp = [nums[i], nums[j], hashMap[complement][k][2], hashMap[complement][k][3]];
                        temp.sort();
                        
                        tempString = temp.toString();
                
                        if (!uniqueMap[tempString]){
                            output.push(temp);
                            uniqueMap[tempString] = 1 ;
                        }
                      
                        
                        
                    }
            }
        }
    }  
    }
    return output;
};
