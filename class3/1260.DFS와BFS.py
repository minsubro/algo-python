import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
_arr = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    _arr[x].append(y)
    _arr[y].append(x)
def dfs(_arr, start):
    visited = []
    stack = deque([start])
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.append(v)
        print(v, end=' ')
        for i in sorted(_arr[v], reverse=True):
            if i not in visited:
                stack.append(i)

def bfs(_arr, start):
    visited = []
    queue = deque([start])
    visited.append(start)
    while queue:
        v = queue.pop()
        for i in sorted(_arr[v]):
            if i not in visited:
                queue.appendleft(i)
                visited.append(i)
        print(v, end=' ')
            
dfs(_arr, v)
print()
bfs(_arr, v)
    