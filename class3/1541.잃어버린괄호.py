import sys

input = sys.stdin.readline
_str = input()
flag = 0
ret = 0
tmp = ""
for s in _str:
    if (s == '+'):
        if flag == 0:
            ret += int(tmp)
        else:
            ret -= int(tmp)
        tmp = ""
    elif (s == '-'):
        if flag == 0:
            ret += int(tmp)
        else:
            ret -= int(tmp)
        flag = 1
        tmp = ""
    else:
        tmp += s
if flag == 0:
    ret += int(tmp)
else:
    ret -= int(tmp)
print(ret)
    