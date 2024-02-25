import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
	_str = input().strip()
	now = 1
	ret = 0
	for s in _str:
		if (s == "O"):
			ret += now
			now += 1
		else:
			now = 1
	print(ret)