import sys
input = sys.stdin.readline
n = int(input())
for i in range(n) :
	r, s = map(str, input().split())
	tmp = ""
	for j in s :
		for k in range(int(r)) :
			tmp += j
	print(tmp)