import sys

def get_gcd(n, m):
	if (m == 0):
		return n
	return get_gcd(m, n % m)

input = sys.stdin.readline
n, m = map(int, input().split())
gcd = get_gcd(n, m)
print(gcd, n * m // gcd, sep='\n')