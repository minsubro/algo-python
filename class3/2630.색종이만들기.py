n = int(input())
blue = 0
white = 0
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def recursive(x, y, n):
    global blue
    global white
    b = True
    w = True
    for i in range(y, y + n):
        for j in range(x, x + n):
            if arr[i][j] == 1:
                w = False
            elif arr[i][j] == 0:
                b = False
    if b == True:
        blue += 1
        return
    elif w == True:
        white += 1
        return
    else:
        recursive(x, y, n // 2)
        recursive(x, y + n // 2, n // 2)
        recursive(x + n // 2, y, n // 2)
        recursive(x + n // 2, y + n // 2, n // 2)
recursive(0, 0, n)
print(white, blue, sep='\n')