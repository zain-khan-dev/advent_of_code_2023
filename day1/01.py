def get_sum(text):
	num = 0
	for c in text:
		if '0' <= c <= '9':
			num += ord(c) - ord('0')
			break
	num *= 10
	for c in text[::-1]:
		if '0' <= c <= '9':
			num += ord(c) - ord('0')
			break
	return num



if __name__ == "__main__":
	total_sum = 0
	with open("01.txt") as file:
		text = file.readlines()
		for line in text:
			total_sum += get_sum(line)
	print(total_sum)