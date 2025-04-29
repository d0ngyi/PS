import sys

n, m = map(int, sys.stdin.readline().split(" "))

a = set(map(int, sys.stdin.readline().split(" ")))
b = set(map(int, sys.stdin.readline().split(" ")))

amb = a.difference(b)
bma = b.difference(a)

print(len(amb) + len(bma))