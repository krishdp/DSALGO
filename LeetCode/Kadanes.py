def kadence(array):
	curr_sum = array[0]
	max_sum = array[0]

	for i in array:
		curr_sum = max(curr_sum + array[i], array[i])
		max_sum = max(max_sum, curr_sum)
	return max_sum


# array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
array = [-1,-2,-3,-4,-5,-6,-7,-8,-9]
print(kadence(array))


















