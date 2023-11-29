import sys

input = sys.stdin.readline
_max = index = 0
for i in range(1, 10):
	n = int(input())
	if (n > _max):
		_max = n
		index = i
print(_max, index, sep='\n')
