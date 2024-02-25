import sys
input = sys.stdin.readline
n = int(input())
cost = [0 for _ in range(301)]
_arr = [0 for _ in range(301)]
for i in range(n):
    cost[i] = int(input())
_arr[0] = cost[0]
_arr[1] = cost[1] + cost[0]
_arr[2] = cost[2] + max(cost[0], cost[1])
for i in range(3, n):
    _arr[i] = cost[i] + max(_arr[i - 2], _arr[i - 3] + cost[i - 1])
print(_arr[n - 1])
