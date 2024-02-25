import sys

input = sys.stdin.readline
while True:
	ret = sum(map(int, input().split()))
	if (ret == 0):
		break
	print(ret)