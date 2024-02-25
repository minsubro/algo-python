import sys
input = sys.stdin.readline

def gcd(x, y):
    if (y == 0): return x
    return gcd(y, x % y)

def lcm(x, y):
    return x * y / gcd(x, y)

tc = int(input())
for _ in range(tc):
    M, N, x, y = map(int, input().split())
    i = x
    tx = ty = 0
    ret = -1
    end = lcm(M, N)
    while True:
        tx = i % M
        ty = i % N
        if (tx == 0): tx = M
        if (ty == 0): ty = N
        if (tx == x and ty == y):
            ret = i
            break
        if (i >= end):
            ret = -1
            break
        i += M
    print(ret)