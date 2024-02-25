import sys
input = sys.stdin.readline
n = int(input())
ret = 0
for i in range(n):
	x1, x2, x3 = map(int, input().split())
	if (x1 == x2 == x3): ret = max(ret, x1 * 1000 + 10000)
	elif (x1 == x2 or x1 == x3 or x2 == x3) :
		if (x1 == x2 or x1 == x3) : ret = max(ret, x1 * 100 + 1000)
		else: ret = max(ret, x2 * 100 + 1000)
	else: ret = max(ret, max(x1, x2, x3) * 100)
print(ret)