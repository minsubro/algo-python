import sys

input = sys.stdin.readline
t = int(input())
arr = [0] * 41
arr[0] = 0
arr[1] = arr[2] = 1
for i in range(3, 41):
    arr[i] = arr[i - 1] + arr[i - 2]
for _ in range(t):
    n = int(input())
    if (n == 0):
        print(1, 0)
    else:
        print(arr[n - 1], arr[n])
    
