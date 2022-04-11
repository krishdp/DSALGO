def next_permutation(n, nums):
    j = 0
    index = 0
    for i in range(n-1, 0, -1):
        if nums[i] > nums[i-1]:
            j = i
        while j < n and nums[j] > nums[i - 1]:
            index = j
            j += 1
        nums[index], nums[i-1] = nums[i-1], nums[index]

        for k in range((n - i)//2):
            nums[i + k], nums[n-1-k] = nums[n-1-k], nums[i + k]
            break
        else:
            nums.reverse()
    return nums


n = int(input("Enter The length of the array: "))
arr = []
for i in range(n):
    i = int(input("Enter the number : "))
    arr.append(i)

print(next_permutation(n, arr))
# print(next_permutation(6, [4, 3, 6, 1, 5, 2]))



# Problem Statement
#
# You are given an array X consisting of permutation of numbers from 1 to N.
# Let there be an array X = [1,2...N] initially.
# You perform the following operation on X array several times :
#
# • You create a new array B as B_Ai = Xi
# • Then you replace Array X with array B.
# For example if you perform the above operation with Array X = [4,6,2,1,5,3] for the first time.
# B_4 = X_1, B_6 = X_2, B_2 = X_3, B_1 = X_4, B_5 = X_5, B_3 = X_6,
# So B becomes : [4,3,6,1,5,2]
# Then we replace X with B, i.e. X becomes = [4,3,6,1,5,2]
#
# Now for each i from 1 to N, you have to tell the number of times the above operation needs to be performed so that X_i becomes equal to i for the first time.
#
# Input Format
#
# • First line contains a single integer denoting N.
# • Next line contains N space-separated integers.
# Output Format
#
# • Print N integers, where the ith integer is equal to number of times the above operation needs to be performed so that Ai becomes equal to its original value for the first time.
# Constraints
#
# • 1<=n<=200
# Sample Input
# 6
# 4 6 2 1 5 3
#
# Sample Output
# 2 3 3 2 1 3
#
# Explanation of Sample
#
# Performing the given operation :
#
# For 1st time   : X = [4,3,6,1,5,2]
# For 2nd time  : X = [1,6,2,4,5,3]
# For 3rd time   : X = [4,2,3,1,5,6]
#
# The highlighted numbers show the first time X_i becomes = i
#
# Hence the answer is = [2,3,3,2,1,3]

