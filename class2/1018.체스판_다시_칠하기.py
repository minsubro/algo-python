import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = []
for i in range(n):
	board.append(input().strip())

def boardCheck(y, x):
	boardSet = ["WBWBWBWB", "BWBWBWBW"]
	cnt1 = cnt2 = 0
	for i in range(8):
		for j in range(8):
			if (i % 2 == 0 and board[i + y][j + x] != boardSet[0][j]):
				cnt1 += 1
			elif (i % 2 == 1 and board[i + y][j + x] != boardSet[1][j]):
				cnt1 += 1
			if (i % 2 == 0 and board[i + y][j + x] != boardSet[1][j]):
				cnt2 += 1
			elif (i % 2 == 1 and board[i + y][j + x] != boardSet[0][j]):
				cnt2 += 1
	return (min(cnt1, cnt2))
				
			


ret = sys.maxsize
for i in range(n - 7):
	for j in range(m - 7):
		ret = min(ret, boardCheck(i, j))
print(ret)
