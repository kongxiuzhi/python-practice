def sumSquare(n):
	if n<0:
		return "small then 0"
	sum = 0
	for i in range(n):
		sum += i * i

	return sum

if __name__ == "__main__":
	print(sumSquare(11))