import sys

input = sys.stdin.readline
n = int(input())
for i in range(n) :
	print("Case #", i + 1, ": ", sum(map(int, input().split())), sep='')