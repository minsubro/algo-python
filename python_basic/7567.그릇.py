import sys

input = sys.stdin.readline
_str = input().strip()
ret = 10
for i in range(1, len(_str)):
    if (_str[i] != _str[i - 1]):
        ret += 10
    else:
        ret += 5
print(ret)
