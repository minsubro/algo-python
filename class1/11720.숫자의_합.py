import sys

input = sys.stdin.readline
n = int(input())
li = list(map(int, input().strip()))
print(sum(li))