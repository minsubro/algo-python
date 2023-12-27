import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
dq = deque()
for _ in range(n):
    oper = list(map(str, input().split()))
    if oper[0] == "push_front":
        dq.appendleft(int(oper[1]))
    elif oper[0] == "push_back":
        dq.append(int(oper[1]))
    elif oper[0] == "pop_front":
        print(-1 if len(dq) == 0 else dq.popleft())
    elif oper[0] == "pop_back":
        print(-1 if len(dq) == 0 else dq.pop())
    elif oper[0] == "size":
        print(len(dq))
    elif oper[0] == "empty":
        print(1 if len(dq) == 0 else 0)
    elif oper[0] == "front":
        print(-1 if len(dq) == 0 else dq[0])
    elif oper[0] == "back":
        print(-1 if len(dq) == 0 else dq[-1])