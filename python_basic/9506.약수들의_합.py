import sys

input = sys.stdin.readline
while True:
    n = int(input())
    li = []
    if (n == -1):
        break
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            li.append(i)
    if n == sum(li):
        print(n, "= ", end='')
        for i in range(len(li)):
            if i != len(li) - 1:
                print(li[i], "+ ", end='')
            else:
                print(li[i])
    else:
        print(n, "is NOT perfect.")
