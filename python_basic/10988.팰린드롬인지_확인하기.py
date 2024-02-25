import sys

input = sys.stdin.readline
_str = input().strip()
_len = len(_str)
for i in range(_len // 2):
	if (_str[i] != _str[_len - i - 1]):
		print(0)
		exit()
print(1)