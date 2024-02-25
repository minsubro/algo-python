import sys

input = sys.stdin.readline
n = int(input())
_set = set()
for i in range(n):
	_set.add(input().strip())
_set = sorted(_set, key=lambda x: (len(x), x))
for i in _set:
	print(i)