from collections import deque

n, k = map(int, input().split())
visit = [-1 for i in range(200001)]
dq = deque([n])
visit[n] = 0
while dq:
    v = dq.pop()
    if (v == k): break
    if (v - 1 >= 0 and visit[v - 1] == -1):
        dq.appendleft(v - 1)
        visit[v - 1] = visit[v] + 1
    if (v + 1 <= 200000 and visit[v + 1] == -1):
        dq.appendleft(v + 1)
        visit[v + 1] = visit[v] + 1
    if (v * 2 <= 200000 and visit[v * 2] == -1):
        dq.appendleft(v * 2)
        visit[v * 2] = visit[v] + 1
print(visit[k])