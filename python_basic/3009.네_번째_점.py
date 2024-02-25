import sys
input = sys.stdin.readline
x = []
y = []
for i in range(3) :
	n, m = map(int, input().split())
	x.append(n)
	y.append(m)
print(x[0] ^ x[1] ^ x[2], y[0] ^ y[1] ^ y[2])