import sys
input = sys.stdin.readline
n = int(input())
i = 1
while (True):
	n -= i
	if (n <= i):
		break
	i += 1
print(i)
