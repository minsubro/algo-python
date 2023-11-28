import sys

input = sys.stdin.readline
n = int(input())
ret = 0
for i in range(n):
    x = int(input())
    if (x == 1):
        ret += 1
    else:
        ret -= 1
if (ret < 0):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
