import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
dq = deque()
for i in range(1, n + 1):
    dq.append(i)
ret = []
while len(dq) != 0:
    for _ in range(1, k):
        dq.append(dq.popleft())
    ret.append(dq.popleft())
print("<", end='')
print(*ret, sep=', ', end='')
print(">")

