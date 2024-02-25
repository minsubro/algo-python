import sys

input = sys.stdin.readline
a, b = int(input()), int(input())
li = list(map(int, str(b)))
print(a * li[2])
print(a * li[1])
print(a * li[0])
print(a * b)