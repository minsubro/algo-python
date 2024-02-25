import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
_map = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
n = int(input())
for _ in range(n):
    v, m = map(int, input().split())
    _map[v].append(m)
    _map[m].append(v)
dq = deque([1])
visit[1] = 1
cnt = 0
while dq:
    v = dq.popleft()
    for i in _map[v]:
        if (visit[i] == 0):
            visit[i] = 1
            dq.append(i)
            cnt += 1
print(cnt)
