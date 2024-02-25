import sys

input = sys.stdin.readline
h, m, s = map(int, input().split())
n = int(input())
s += n
m += int(s / 60)
h += int(m / 60)
print(h % 24, m % 60, s % 60)