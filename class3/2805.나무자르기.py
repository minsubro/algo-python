import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = list(map(int, input().split()))
_min = 0
_max = max(li)
ret = 0
while True:
    if (_min > _max):
        break
    mid = (_min + _max) // 2
    cnt = 0
    for i in li:
        if (i > mid):
            cnt += i - mid
    if (cnt < m):
        _max = mid - 1
    else:
        ret = mid
        _min = mid + 1
print(ret)