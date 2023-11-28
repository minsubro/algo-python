import sys
input = sys.stdin.readline
ret = 0
for i in range(5) :
	n = int(input())
	ret += max(40, n)
print(int(ret / 5))
	