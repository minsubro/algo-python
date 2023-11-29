import sys

input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
arr = [0 for i in range(10)]
li = list(map(int, str(a * b * c)))
for i in li:
	arr[i] += 1
for i in arr:
	print(i)