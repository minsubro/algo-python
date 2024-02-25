import sys
from collections import deque
input = sys.stdin.readline
udlr = [[1, 0], [0, 1], [-1, 0], [0, -1]]
n = int(input())
_map = []
for _ in range(n):
    _map.append(input().strip())
total = 0
visit = [[0 for _ in range(n)] for _ in range(n)]
ret = []
for i in range(n):
    for j in range(n):
        if (_map[i][j] == '1' and visit[i][j] == 0):
            dq = deque([[i, j]])
            visit[i][j] = 1
            cnt = 1
            total += 1
            while dq:
                y, x = dq.popleft()
                for a, b in udlr:
                    n_x = x + a
                    n_y = y + b
                    if n_x < 0 or n_x >= n or n_y < 0 or n_y >=n:
                        continue
                    if _map[n_y][n_x] == '1' and visit[n_y][n_x] == 0:
                        visit[n_y][n_x] = 1
                        dq.append([n_y, n_x])
                        cnt += 1
            ret.append(cnt)
print(total, *sorted(ret), sep='\n')