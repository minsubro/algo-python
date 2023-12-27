import sys

input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))
li.sort(key=lambda x: (x[0], x[1]))
for x, y in li:
    print(x, y)
