import sys

input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    _num, name = map(str, input().split())
    li.append([int(_num), name])
li.sort(key=lambda x: x[0])
for num, name in li:
    print(num, name)