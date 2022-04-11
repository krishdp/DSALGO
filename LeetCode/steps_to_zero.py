# Steps to Zero
# Problem Statement
#
# You are given an array A of size N. In one step you can chose any non-negative 
# integer X (X>=0) and convert all the elements A_i (1<=i<=N) that are greater 
# than or equal to X to X. The cost of this step will be:
#
# 𝑁 ∑𝑚𝑎𝑥(0, 𝐴_𝑖 − 𝑋) 𝑖=1
#
# For Example, Let the array be A = [ 1, 4,3 ,6 ] and we chose X = 2. 
# Then array would be converted to A=[ 1,2,2,2] and cost for this 
# step will be 0 + (4-2) + (3-2) + (6-2) = 7.

#
# You have to make all the elements of the array 0 by using these steps. But the cost 
# of each step should not exceed K (K>=N).
#
# Find the minimum number of steps required to make all the elements of the array 0.
#
# Constraints
#
# • 1 <= N <= 10^5 • N <= K <= 10^9 • 1 <= Ai <= 10^5
#
# Input Format
#
# • First-line contains two space separated integers N and K.
#
# • Next line contains N space separated integers denoting A_1,A_2,…......A_N.
#
# Output Format
#
# • Print a single integer denoting minimum number of steps required to make all the elements of the array 0.
#
# Sample Input  no of test case - 1  
#                          no  Of elements - 3
                             # 3  

                              3 1 2
#
# Sample Output 1 2
#
# Explanation of Sample 1
#
# In First step we chose X = 1, the array becomes [1,1,1] and cost is (3-1)+0+(2-1) = 3(<=K)
#
# In Second step we chose X = 0, the array becomes [0,0,0] and cost is (1-0)+(1- 0)+(1-0) = 3(<=K)
#
# So it takes 2 steps



def Solution(arr):
    total = 0
    cur = 0
    X = 0
    arr1 = []
    for i in arr:
        if i not in arr1:
            arr1.append(i)
        else:
            continue

    for i in range(1, len(arr1)):
        if arr1[i] > X:
            cur = arr1[i] - X
        elif arr1p[i] <= X:
            cur = 0
        total += cur
        X += 1

    return total


print(Solution([1, 4, 3, 6]))
