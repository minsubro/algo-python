import sys

input = sys.stdin.readline
M = 1234567891
r = 31
n = int(input())
_str = str(input().strip())
ret = 0
for i in range(0, n):
    ret += (ord(_str[i]) - 96) * (r ** i)
print(ret % M)