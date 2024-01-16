import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())
ret = 0
while n > 0:
    if ((2 ** (n - 1)) <= r):
        r -= 2 ** (n - 1)
        ret += (2 ** n) * (2 ** (n - 1))
    if ((2 ** (n - 1)) <= c):
        c -= 2 ** (n - 1)
        ret += (2 ** (n - 1)) * (2 ** (n - 1))
    n -= 1
print(ret)