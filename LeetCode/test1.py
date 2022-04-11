def Solution(n, arr):
	total = 0
	cur_sum = 0
	for i in range(n):
		cur_sum = arr[i] * (sum(arr) - arr[i])
		total += cur_sum
	return total


n = int(input("Enter The length of the array"))
arr = []
for i in range(n):
	i = int(input("Enter the number : "))
	arr.append(i)

print(Solution(n, arr))
# print(Solution(4, [4, 3, 5, 1]))


# Problem Statement
#
# There are N people in a room. Everyone of them is infected by a virus and the power of virus inside everyone is given in the form of an array of size N. Every person in the room shakes hands with one another such that each and every person has shaken hands with exactly N-1 people.
# Suppose there is person A with a virus of power a and another person B with virus of power b. If both of them shake hands with each other then person A will have a virus of power b accumulated on his hand and b will have virus of power a on his hand. Now A decides to shake hands with person C with a virus of power c. After both of them shake hands C will have virus of power a on his hands and A will have virus of power (b+c) accumulated on his hands.
# After everyone in the room shakes hands with each other and a certain amount of time passes, the virus accumulated on their hands starts entering their body and then the pre-existing virus and the total accumulated virus mutate such that the power of the virus in the person will become the product of the powers of pre-existing and accumulated viruses. You need to find the total sum power of viruses in the room.
#
#
# Constraints
#
# 1 N 10^6
# 1 A[i] 10^6 where A[i] power of virus in a person.
#
#
# Input Format
#
# First line contains a single integer N (number of people).
# Second line contains N spaced integers representing the power of virus in each person.
#
#
# Output Format
#
# Print the total sum power of viruses in the room.
#
#
# Sample Input
#
# 4
# 4 3 5 1
#
#
# Sample Output
# 118
#
# Explanation of Sample
# Power of virus in first person => 4*(3+5+1) =>36
# Power of virus in second person => 3*(4+5+1) =>30
# Power of virus in third person => 5*(4+3+1) =>40
# Power of virus in fourth person => 1*(4+3+5) =>12
# Total virus in the room = 36+30+40+12 => 118