import sys
input = sys.stdin.readline
ch = int(input())
n = int(input())
button = set([i for i in range(0, 10)])
if n != 0: remove = list(map(int, input().split()))
for i in range(n):
    button.remove(remove[i])
click = abs(100 - ch)
for i in range(0, (ch * 2) + 101):
    tmp_set = set(list(map(int, str(i))))
    diff = tmp_set - button
    if (len(diff) == 0):
        click = min(click, len(list(map(int, str(i)))) + int(abs(ch - i)))
print(click)