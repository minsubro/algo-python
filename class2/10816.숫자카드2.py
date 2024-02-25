import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dic = dict()
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    print(dic[i] if i in dic else 0, end=' ')
