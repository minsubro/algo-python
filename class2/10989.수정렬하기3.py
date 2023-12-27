import sys

input = sys.stdin.readline
n = int(input())
li = [0] * 10001
for _ in range(n):
    li[int(input())] += 1
for i in range(1, 10001):
    if (li[i] > 0):
        for _ in range(li[i]):
            print(i)
            