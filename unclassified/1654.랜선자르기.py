import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
	arr.append(int(input()))
arr.sort()
print(arr)