import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
dic = dict()
ret = []
for _ in range(n):
    name = input().strip()
    dic[name] = 1
for _ in range(m):
    name = input().strip()
    if name in dic:
        ret.append(name)
ret.sort()
print(len(ret), *ret, sep='\n')