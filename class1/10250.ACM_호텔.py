import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
	h, w, n = map(int, input().split())
	ret = 0
	if (n % h == 0):
		ret += (h * 100) + (n // h)
	else:
		ret += n % h * 100
		ret += n // h + 1
	print(ret)