import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n * 2)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
_min = sys.maxsize
ret = 0
for i in range(1, n + 1):
    visit = [-1] * (n + 1)
    queue = deque([i])
    visit[i] = 0
    while queue:
        v = queue.pop()
        for j in graph[v]:
            if visit[j] == -1:
                visit[j] = visit[v] + 1
                queue.appendleft(j)
    _sum = sum(visit)
    if _sum < _min:
        _min = _sum
        ret = i
print(ret)