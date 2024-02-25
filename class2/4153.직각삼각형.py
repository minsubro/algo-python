import sys

input = sys.stdin.readline
while True:
	li = sorted(list(map(int, input().split())))
	if (li[0] == li[1] == li[2] == 0):
		break
	if (li[0] ** 2 + li[1] ** 2 == li[2] ** 2):
		print("right")
	else:
		print("wrong")