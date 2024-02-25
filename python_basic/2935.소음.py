import sys
input = sys.stdin.readline
n = int(input())
oper = str(input().strip())
m = int(input())
if (oper == '*'): print(n * m)
elif (oper == '+'): print(n + m)