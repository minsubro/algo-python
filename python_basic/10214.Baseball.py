import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
	yonsei = korea = 0
	for i in range(9):
		x, y = map(int, input().split())
		yonsei += x
		korea +=  y
	if (yonsei == korea):
		print("Draw")
	elif (yonsei > korea):
		print("Yonsei")
	else:
		print("Korea")