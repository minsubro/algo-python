import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
	m = int(input())
	ret = ""
	_max = int(0)
	for i in range(m):
		name, s = map(str, input().strip().split())
		if int(s) > _max:
			_max = int(s)
			ret = name
	print(ret)