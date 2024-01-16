import sys
input = sys.stdin.readline
print = sys.stdout.write
_set = set()
n = int(input())
for _ in range(n):
    oper = list(map(str, input().split()))
    if (oper[0] == "add"):
        _set.add(int(oper[1]))
    elif (oper[0] == "remove"):
        if int(oper[1]) in _set:
            _set.remove(int(oper[1]))
    elif (oper[0] == "check"):
        if int(oper[1]) in _set:
            print("1\n")
        else:
            print("0\n")
    elif (oper[0] == "toggle"):
        if int(oper[1]) in _set:
            _set.remove(int(oper[1]))
        else:
            _set.add(int(oper[1]))
    elif (oper[0] == "all"):
        for i in range(1, 21):
            _set.add(i)
    elif (oper[0] == "empty"):
        _set.clear()
