def compare(x, y):
	if x > y:
		return 1
	if x == y:
		return 0
	if x < y:
		return -1

print compare(1, 2)
print compare(1, 1)
print compare(2, 1)