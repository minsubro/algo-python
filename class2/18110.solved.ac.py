import sys

EPS = 1e-9
input = sys.stdin.readline
n = int(input())
a = round((n * 0.15) + EPS)

arr = []
if n == 0:
    print(0)
    exit()
for _ in range(n):
    arr.append(int(input()))
arr.sort()
ret = 0
for i in range(a, n - a):
    ret += arr[i]
print(round((ret / (n - (a * 2))) + EPS))