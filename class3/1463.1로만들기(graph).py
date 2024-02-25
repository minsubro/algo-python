from collections import deque

n = int(input())
visit = [-1] * (n + 1)
queue = deque([n])
visit[n] = 0
while queue:
    v = queue.pop()
    if (v == 1):
        break
    if (v > 0 and visit[v - 1] == -1):
        queue.appendleft(v - 1)
        visit[v - 1] = visit[v] + 1
    if (v % 3 == 0 and visit[v // 3] == -1):
        queue.appendleft(v // 3)
        visit[v // 3] = visit[v] + 1
    if (v % 2 == 0 and visit[v // 2] == -1):
        queue.appendleft(v // 2)
        visit[v // 2] = visit[v] + 1
print(visit[1])