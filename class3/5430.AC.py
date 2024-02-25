import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    oper = input().strip()
    n = int(input())
    _str = input().strip()
    dq = deque()
    tmp = ""
    error = False
    reverse = False
    for i in range(1, len(_str) - 1):
        if (_str[i] == ','):
            dq.append(int(tmp))
            tmp = ""
        else:
            tmp += _str[i]
    if len(tmp):
        dq.append(int(tmp))
    for command in oper:
        if command == 'R':
            if reverse:
                reverse = False
            else:
                reverse = True
        elif command == 'D':
            if len(dq) == 0:
                print("error")
                error = True
                break
            if reverse: 
                dq.pop()
            else:
                dq.popleft()
    if not error:
        if reverse:
            dq.reverse()
        print("[", end='')
        print(*dq, sep=',', end='')
        print("]",)