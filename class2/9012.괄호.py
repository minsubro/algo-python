import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    _str = input().strip()
    cnt = 0
    ret = True
    for i in _str:
        if i == "(":
            cnt += 1
        else:
            if (cnt == 0):
                ret = False
            cnt -= 1
    if (cnt != 0):
        ret = False
    print("YES" if ret else "NO")
    
        