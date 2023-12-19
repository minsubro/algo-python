import sys

input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    oper = list(map(str, input().split()))
    if oper[0] == "push":
        stack.append(oper[1])
    elif oper[0] == "pop":
        print(-1 if len(stack) == 0 else stack.pop())
    elif oper[0] == "size":
        print(len(stack))
    elif oper[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif oper[0] == "top":
        print(-1 if len(stack) == 0 else stack[-1])