# ["Encrypter", "encrypt", "decrypt"]
# [[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]



def encrypt(keys, values, msg):
	encrypt_dict = {}
	for (i, j) in zip(keys, values):
		encrypt_dict[i] = j

	encrypt_msg = ""
	for i in msg:
		if i in encrypt_dict:
			encrypt_msg += encrypt_dict[i]
	return encrypt_msg


def decrypt(keys, values, dictionary, encrypt_msg):
	decrypt_dict = {}
	for (i, j) in zip(keys, values):
		decrypt_dict[i] = j

	decrypt_msg_list = []
	# for i in range(len(encrypt_msg)-1):
	curr = 0
	while curr < len(encrypt_msg)-1:
		sub_str = encrypt_msg[curr:curr+2]
		decrypt_msg_list.append(sub_str)
		curr += 2
	test = []
	for i in decrypt_msg_list:
		if i in values:
			index = values.index(i)
			test.append(index)

	return test





keys = ['a', 'b', 'c', 'd']
values = ["ei", "zf", "ei", "am"]

dictionary = ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]

print(encrypt(keys, values, "abcd"))
print(decrypt(keys, values, dictionary, "eizfeiam"))


class Encrypter:
	def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
		self.hashmap = dict()
		for i in range(len(keys)):
			self.hashmap[keys[i]] = values[i]
		self.dictmap = defaultdict(int)
		for word in dictionary:
			self.dictmap[self.encrypt(word)] += 1

	def encrypt(self, word1: str) -> str:
		output = ''
		for char in word1:
			output += self.hashmap[char]
		return output

	def decrypt(self, word2: str) -> int:
		return self.dictmap[word2]











