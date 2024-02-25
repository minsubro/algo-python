import sys

input = sys.stdin.readline
arr = [[0] * 15 for _ in range(15)]
arr[0] = list(range(0, 16))
for i in range(1, 15):
	for j in range(1, 15):
		arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
tc = int(input())
for _ in range(tc):
	k = int(input())
	n = int(input())
	print(arr[k][n])
	