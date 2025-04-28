import sys

n = list(map(int, sys.stdin.readline().rstrip()))

n.sort(reverse=True)
for i in range(0, len(n)):
    print(n[i], end="")