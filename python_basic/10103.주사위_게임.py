import sys

input = sys.stdin.readline
n = int(input())
a = b = 100
for i in range(n):
	x, y = map(int, input().split())
	if (x < y):
		a -= y
	elif(x > y):
		b -= x
print(a, b, sep='\n')