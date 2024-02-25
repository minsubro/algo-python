import sys

input = sys.stdin.readline
li = list(map(int, input().split()))
li = [i * i for i in li]
print(sum(li) % 10)