
def fourSum(nums, target):
    N = len(nums)
    if N < 4:
        return []
    res = []
    nums = sorted(nums)
    i = 0
    for i in range(N-3):
        if 0 < i < N-3 and nums[i] == nums[i-1]:
            continue        
        for j in range(i+1,N-2):
            if i+1 < j < N-2 and nums[j] == nums[j-1]:
                continue
            k = j+1
            l = N-1
            while k < l:
                summ = nums[i]+nums[j]+nums[k]+nums[l]
                if summ == target:
                    res.append([nums[i],nums[j],nums[k],nums[l]])
                    while k < N-1 and nums[k] == nums[k+1]:
                        k += 1
                    while l > 0 and nums[l] == nums[l-1]:
                        l -= 1
                    k += 1
                    l -= 1
                elif summ < target:
                    k += 1
                else:
                    l -= 1
    return res
print(fourSum([1,0,-1,0,-2,2], 0))