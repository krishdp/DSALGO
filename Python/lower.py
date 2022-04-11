def lower(str):
	num = 0
	res = ''
	for i in str:
		num = ord(i)
		asci = num + 32
		res += chr(asci)

	return res

print(lower('HELLO'))