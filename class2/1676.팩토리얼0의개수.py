import sys

input = sys.stdin.readline
n = int(input())
ret = 1
for i in range(1, n + 1):
	ret *= i	
li = list(map(int, str(ret)))
cnt = 0
for i in li[::-1]:
	if (i != 0):
		break
	cnt += 1
print(cnt)