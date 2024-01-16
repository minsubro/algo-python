import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic1 = dict()
dic2 = dict()
for i in range(1, n + 1):
    poketmon = input().strip()
    dic1[poketmon] = i
    dic2[i] = poketmon
for _ in range(m):
    _input = input().strip()
    if _input.isdigit():
        print(dic2[int(_input)])
    else:
        print(dic1[_input])