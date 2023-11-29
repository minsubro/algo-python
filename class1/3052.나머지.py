import sys

input = sys.stdin.readline
arr = [0 for i in range(42)]
for i in range(10):
	arr[int(input()) % 42] += 1
print(42 - arr.count(0))