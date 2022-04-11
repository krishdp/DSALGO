def sqrt(n):
	result = 0
	num = n - 1
	while num > 0:
		if num * num <= n:
			result = num
		else:
			num = num - 1
	return result

print(sqrt(8))