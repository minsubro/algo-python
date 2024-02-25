import sys

input = sys.stdin.readline
_str = input().strip()
arr = [-1 for i in range(26)]
for i in range(len(_str)):
	index = (ord(_str[i]) - 97)
	if arr[index] == -1:
		arr[index] = i
for i in range(26):
	print(arr[i], end=' ')