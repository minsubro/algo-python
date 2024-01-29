import sys
input = sys.stdin.readline
n = int(input())
length = int(input())
string = input().strip()
cnt = 0
compare = "OI"
a = 0
i = 0
while i < length - 2:
    if (string[i] == 'I' and string[i + 1] + string[i + 2] == compare):
        i += 2
        a += 1
    else:
        if (a - n >= 0):
            cnt += a - n + 1
        i += 1
        a = 0
if (a - n >= 0):
    cnt += a - n + 1
print(cnt)
        