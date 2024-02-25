import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
_max = max(arr)
arr = [i / _max * 100 for i in arr]
print(sum(arr) / n)