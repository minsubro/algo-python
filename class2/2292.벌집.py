import sys

input = sys.stdin.readline
n = int(input())
cnt = 1
_sum = 1
i = 1
while True:
	if n <= _sum:
		break
	_sum += i * 6
	i += 1
	cnt += 1
print(cnt)