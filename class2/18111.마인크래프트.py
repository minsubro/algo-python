import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
height = 0
time = sys.maxsize
for i in range(257):
    dig = 0
    stack = 0
    for _arr in arr:
        for value in _arr:
            if (value < i):
                stack += i - value
            elif (value > i):
                dig += value - i
    if (stack > dig + b):
        continue
    elif ((dig * 2) + stack <= time):
        time = dig * 2 + stack
        height = i
print(time, height)