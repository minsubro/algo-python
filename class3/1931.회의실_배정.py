import sys
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))
li.sort(key=lambda x: (x[1], x[0]))
cnt = 0
refer = 0
for i in range(n):
    if (li[i][0] >= refer):
        refer = li[i][1]
        cnt += 1
print(cnt)