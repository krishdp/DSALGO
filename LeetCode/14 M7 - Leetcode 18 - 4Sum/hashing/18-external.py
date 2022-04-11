import collections


def fourSum(nums, target):
    nums.sort()
    if len(nums) < 4 or 4*nums[0] > target or 4*nums[-1] < target: return []
    total_map = collections.defaultdict(list)
    results = set()
    
    for num1 in range(len(nums)-1):
        for num2 in range(num1 + 1, len(nums)):
            diff = target - nums[num1] - nums[num2]
            total_map[diff].append((num1, num2))

                
    for num1 in range(len(nums) - 3):
        for num2 in range(num1 + 1, len(nums)):
            total = nums[num1] + nums[num2]
            if total in total_map:
                for pair in total_map[total]:
                    if pair[0] > num2:
                        results.add((nums[num1], nums[num2], nums[pair[0]], nums[pair[1]]))
    
    return [list(result) for result in results]


print(fourSum([1,0,-1,0,-2,2], 0))