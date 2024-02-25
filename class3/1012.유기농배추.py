import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
udlr =[[1, 0], [0, 1], [-1, 0] , [0, -1]]
for _ in range(t):
    col, row, k = map(int, input().split())
    arr = [[0 for _ in range(col)] for _ in range(row)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    cnt = 0
    for i in range(row):
        for j in range(col):
            if (arr[i][j] == 1):
                cnt += 1
                arr[i][j] = 0
                dq = deque()
                dq.append([i, j])
                while len(dq):
                    now = dq.popleft()
                    for t_y, t_x in udlr:
                        if (now[0] + t_y < row and now[0] + t_y >= 0 and now[1] + t_x < col and now[1] + t_x >= 0):
                            if (arr[now[0] + t_y][now[1] + t_x] == 1):
                                arr[now[0] + t_y][now[1] + t_x] = 0
                                dq.append([now[0] + t_y, now[1] + t_x])
    print(cnt)
                
                