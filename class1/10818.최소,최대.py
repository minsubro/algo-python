import sys

input = sys.stdin.readline
n = int(input())
li = sorted(list(map(int, input().split())))
print(li[0], li[len(li) - 1])