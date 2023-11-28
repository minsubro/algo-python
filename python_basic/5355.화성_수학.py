import sys
input = sys.stdin.readline
n = int(input())
for i in range(n) :
	li = list(map(str, input().split()))
	num = 0
	for i in range(len(li)) :
		if (i == 0) : num = float(li[i])
		else :
			if (li[i] == '@') : num *= 3
			elif (li[i] == '%') : num += 5
			elif (li[i] == '#') : num -= 7
	print(f'{num:.2f}')