import sys

input = sys.stdin.readline
arr = [0 for i in range(26)]
_str = str(input().strip()).lower()
_max = 0
for i in _str :
	arr[ord(i) - 97] += 1
	_max = max(_max, arr[ord(i) - 97])
if (arr.count(_max) != 1):
	print("?")
else:
	print(chr(arr.index(_max) + 65))