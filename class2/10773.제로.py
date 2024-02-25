import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    _num = int(input())
    if _num == 0:
        stack.pop()
    else:
        stack.append(_num)
print(sum(stack))