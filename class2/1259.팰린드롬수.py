import sys

input = sys.stdin.readline
while True:
	n = list(map(int, input().strip()))
	ret = True
	if (n[0] == 0):
		break
	_len = len(n)
	for i in range(_len // 2):
		if (n[i] != n[_len - i - 1]):
			ret = False
			break
	if (ret):
		print("yes")
	else: print("no")

	