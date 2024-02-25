import sys
input = sys.stdin.readline
n = int(input())
string = input().strip()
a = string.count('A')
b = string.count('B')
if (a == b):
    print("Tie")
elif (a > b):
	print("A")
else:
	print("B")
