import sys

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

input = sys.stdin.readline
n = int(input())
for i in range(n):
	a, b = map(int, input().split())
	print (a * b // gcd(a, b))
	