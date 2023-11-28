import sys
input = sys.stdin.readline
x1, x2, x3 = map(int, input().split())
if (x1 == x2 == x3): print(x1 * 1000 + 10000)
elif (x1 == x2 or x1 == x3 or x2 == x3) :
	if (x1 == x2 or x1 == x3) : print (x1 * 100 + 1000)
	else: print(x2 * 100 + 1000)
else:print(max(x1, x2, x3) * 100)