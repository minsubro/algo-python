import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
_min = sys.maxsize
ret = 0
for i in range(0, n):
	for j in range(i + 1, n):
		for k in range(j + 1, n):
			_sum = arr[i] + arr[j] + arr[k]
			if _sum <= m :
				if m - _sum < _min:
					ret = _sum
					_min = m - _sum
print(ret)