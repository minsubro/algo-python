import sys
input = sys.stdin.readline
h, m = map(int, input().split())
n = int(input())
print((h + int(((n + m) / 60))) % 24, (n + m) % 60)
