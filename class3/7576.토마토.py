import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
_map = []
dxdy =  [[1, 0], [0, 1], [-1, 0], [0, -1]]
visit = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(m):
    _map.append(list(map(int, input().split())))
dq = deque()
for y in range(m):
    for x in range(n):
        if (_map[y][x] == 1):
            dq.appendleft([x, y])
while dq:
    x, y = dq.pop()
    for dx, dy in dxdy:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if (_map[ny][nx] == 0):
            dq.appendleft([nx, ny])
            _map[ny][nx] = _map[y][x] + 1
ret = 0
ret2 = True
for arr in _map:
    ret = max(ret, max(arr))
    if 0 in arr:
        ret2 = False
print(ret - 1 if ret2 == True else -1)